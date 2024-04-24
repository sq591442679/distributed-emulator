/**
 * in order to count ttl loss:
 * 	use use krpobe to monitor ip_forward() to check ttl
 * in order to count no-entry loss:
 * 	1. use kretprobe to monitor kernel function ip_route_input_slow(), focusing on res->type (for intermediate satellites)
 * 	2. use kretprobe to monitor kernel function ip_route_output_flow(), focusing on IS_ERR(rt) (for udp sender satellites, but not for sure)
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/atmioc.h>
#include <linux/ktime.h>

#include <linux/types.h>
#include <linux/mm.h>
#include <linux/skbuff.h>
#include <linux/ip.h>
#include <linux/icmp.h>
#include <linux/netdevice.h>
#include <linux/ftrace.h>
#include <linux/slab.h>
#include <net/sock.h>
#include <net/ip.h>
#include <net/tcp.h>
#include <net/udp.h>
#include <net/icmp.h>
#include <linux/tcp.h>
#include <linux/udp.h>
#include <linux/netfilter_ipv4.h>
#include <net/checksum.h>
#include <linux/route.h>
#include <net/route.h>
#include <net/xfrm.h>
#include <net/rtnetlink.h>

static const int MAIN_TABLE_ID = 254;
static __be32 dst_ip = 0u;

module_param(dst_ip, uint, S_IRUGO);
MODULE_PARM_DESC(dst_ip, "data packet destination used for packet drop monitor");

static atomic64_t ttl_drop_cnt = ATOMIC64_INIT(0);
static atomic64_t no_entry_cnt = ATOMIC64_INIT(0);

static unsigned long long get_epoch_time_ns(void)
{
	// return the time through Unix epoch in seconds
	ktime_t now = ktime_get_real();
	unsigned long long ns = ktime_to_ns(now);
	return ns;
}

static int ip_forward_pre_handler(struct kprobe *p, struct pt_regs *regs)
{
	if (regs != NULL) {
		struct sk_buff *skb = (struct sk_buff *)regs->di;
		if (skb != NULL && ip_hdr(skb) != NULL) {
			if (ip_hdr(skb)->ttl <= 1) {
				struct net *net = dev_net(skb->dev);
				if (net != NULL && net != &init_net) {
					__be32 satellite_id = net->satellite_id;
					pr_info("%s,%pI4,%llu,ttl\n", __func__, &satellite_id, get_epoch_time_ns());

					atomic64_inc(&ttl_drop_cnt);
				}
			}		
		}
			
	}
    return 0;   
}

struct ip_route_input_slow_data {
	struct sk_buff *skb;
	__be32 daddr;
	struct net_device *dev;
	struct fib_result *res;
};

struct ip_route_output_flow_data {
	struct net *net;
	struct flowi4 *flp4;
};

static int ip_route_input_slow_entry_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
	struct ip_route_input_slow_data *data = (struct ip_route_input_slow_data *)ri->data;
	if (data != NULL && regs != NULL) {
		data->skb = (struct sk_buff *)regs->di;
		data->daddr = (__be32)regs->si;
		data->dev = (struct net_device *)regs->r8;
		data->res = (struct fib_result *)regs->r9;
		// pr_info("%s    %p    %p\n", __func__, data->dev, data->res);
	}
	return 0;
}

static int ip_route_input_slow_ret_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
	struct ip_route_input_slow_data *data = (struct ip_route_input_slow_data *)ri->data;
	if (regs != NULL && data != NULL) {
		struct sk_buff *skb = data->skb;
		__be32 daddr = data->daddr;
		struct net_device *dev = data->dev;
		struct fib_result *res = data->res;
		if (res != NULL && skb != NULL && dev != NULL) {
			struct net *net = dev_net(dev);
			unsigned char type = res->type;
			// pr_info("%s   %p\n", __func__, res);
			// pr_info("%s      daddr: %pI4, net:%p, res: %p, type:%u\n", __func__, &daddr, net, res, type);
			if (daddr == dst_ip && 
				(type == RTN_BLACKHOLE || type == RTN_UNREACHABLE || type == RTN_PROHIBIT || type == RTN_THROW)) {
				if (net != NULL && net != &init_net) {
					__be32 satellite_id = net->satellite_id;
					if (satellite_id != 0x7f7f7f7f) {
						pr_info("%s,%pI4,%llu,no entry\n", __func__, &satellite_id, get_epoch_time_ns());

						atomic64_inc(&no_entry_cnt);
					}
				}
			}
		}
		else {
			pr_err("%s res is NULL\n", __func__);
		}
	}
	else {
		pr_err("%s regs is NULL\n", __func__);
	}

    return 0;
}

static int ip_route_output_flow_entry_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
	struct ip_route_output_flow_data *data = (struct ip_route_output_flow_data *)ri->data;
	if (regs != NULL && data != NULL) {
		data->net = (struct net *)regs->di;
		data->flp4 = (struct flowi4 *)regs->si;
	}
	return 0;
}

static int ip_route_output_flow_ret_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
	struct ip_route_output_flow_data *data = (struct ip_route_output_flow_data *)ri->data;
	if (regs != NULL && data != NULL) {
		struct rtable *rt = (struct rtable *)regs->ax;
		struct net *net = data->net;
		struct flowi4 *flp4 = data->flp4;
		if (rt) {
			// pr_info("%s    net:%p  flp4:%p  rt:%p\n", __func__, net, flp4, rt);
			if (net != NULL && net != &init_net) {
				if (flp4 != NULL) {
					__be32 daddr = flp4->daddr;
					if (daddr == dst_ip) {
						if (IS_ERR(rt)) {
							__be32 satellite_id = net->satellite_id;
							if (satellite_id != 0x7f7f7f7f) {
								pr_info("%s,%pI4,%llu,no entry\n", __func__, &satellite_id, get_epoch_time_ns());

								atomic64_inc(&no_entry_cnt);
							}
						}			
					}
				}
			}
		}
		else {
			pr_err("%s rt is NULL\n", __func__);
		}
	}
	return 0;
}

static struct kprobe kp_ip_forward = {
    .symbol_name = "ip_forward",
	.pre_handler = ip_forward_pre_handler,
};

static struct kretprobe krp_ip_route_input_slow = {
    .kp.symbol_name = "ip_route_input_slow",
    .maxactive = NR_CPUS,
	.data_size = sizeof(struct ip_route_input_slow_data),
	.handler = ip_route_input_slow_ret_handler,
	.entry_handler = ip_route_input_slow_entry_handler,
};

static struct kretprobe krp_ip_route_output_flow = {
	.kp.symbol_name = "ip_route_output_flow",
	.maxactive = NR_CPUS,
	.data_size = sizeof(struct ip_route_output_flow_data),
	.handler = ip_route_output_flow_ret_handler,
	.entry_handler = ip_route_output_flow_entry_handler,
};

static int packet_drop_module_init(void)
{
    int ret;

    ret = register_kprobe(&kp_ip_forward);
	if (ret < 0) {
        pr_err("register_kprobe kp_ip_forward failed\n");
        return -1;
    }
    else {
        pr_info("planted kprobe kp_ip_forward at %p\n", kp_ip_forward.addr);
    }

	ret = register_kretprobe(&krp_ip_route_input_slow);
	if (ret < 0) {
        pr_err("register_kretprobe krp_ip_route_input_slow failed\n");
        return -1;
    }
    else {
        pr_info("planted kretprobe krp_ip_route_input_slow at %p\n", krp_ip_route_input_slow.kp.addr);
    }

	ret = register_kretprobe(&krp_ip_route_output_flow);
	if (ret < 0) {
        pr_err("register_kretprobe krp_ip_route_output_flow failed\n");
        return -1;
    }
    else {
        pr_info("planted kretprobe krp_ip_route_output_flow at %p\n", krp_ip_route_output_flow.kp.addr);
    }

    return 0;
} 

static void packet_drop_module_exit(void)
{
	pr_info("ttl exceed packet cnt: %lld\n", atomic64_read(&ttl_drop_cnt));
	unregister_kprobe(&kp_ip_forward);
    pr_info("%s	unregisterd kp_ip_forward\n", __func__);

    pr_info("no entry packet cnt: %lld\n", atomic64_read(&no_entry_cnt));
	unregister_kretprobe(&krp_ip_route_input_slow);
	pr_info("%s	unregisterd krp_ip_route_input_slow\n", __func__);

	unregister_kretprobe(&krp_ip_route_output_flow);
    pr_info("%s	unregisterd krp_ip_route_output_flow\n", __func__);
}

module_init(packet_drop_module_init);
module_exit(packet_drop_module_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");