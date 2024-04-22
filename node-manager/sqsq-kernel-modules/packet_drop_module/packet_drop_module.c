/**
 * TODO: to count no-entry loss:
 * 1. use kretprobe to monitor kernel function ip_route_input_slow(), focusing on res->type (for intermediate satellites)
 * 2. use kretprobe to monitor kernel function ip_route_output_flow(), focusing on IS_ERR(rt) (for udp sender satellites, but not for sure)
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/atmioc.h>

#include <linux/types.h>
#include <linux/mm.h>
#include <linux/skbuff.h>
#include <linux/ip.h>
#include <linux/icmp.h>
#include <linux/netdevice.h>
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

static struct kprobe kp_ip_forward = {
    .symbol_name = "ip_forward",
};

struct my_data {    // used to record parameter of ip_route_input_slow and 
    struct fib_table *tb;
    struct fib_result *res;
    struct flowi4 *flp;
};

static struct kretprobe krp_ip_route_input_slow = {
    .kp.symbol_name = "ip_route_input_slow",
    .maxactive = NR_CPUS,
    .data_size = sizeof(struct my_data),
};

static struct kretprobe krp_ip_route_output_flow = {
	.kp.symbol_name = "ip_route_output_flow",
	.maxactive = NR_CPUS,
};

static int ip_forward_pre_handler(struct kprobe *p, struct pt_regs *regs)
{
    struct sk_buff *skb = (struct sk_buff *)regs->di;

	if (ip_hdr(skb)->ttl <= 1) {
		atomic64_inc(&ttl_drop_cnt);
		// pr_info("current ttl ttl_drop_cnt: %lld\n", ttl_drop_cnt);
	}

    return 0;   
}

static int ip_route_input_slow_ret_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
    struct fib_result *res;
	uint8_t type;
	if (regs) {
		res = (struct fib_result *)regs->r9;
		if (res) {
			type = res->type;
			pr_info("%s      res: %p, type:%u\n", __func__, res, type);
			if (type == RTN_BLACKHOLE || type == RTN_UNREACHABLE || type == RTN_PROHIBIT || type == RTN_THROW) {
				atomic64_inc(&no_entry_cnt);
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

static int ip_route_output_flow_ret_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
	struct rtable *ret;
	if (regs) {
		ret = (struct rtable *)regs->ax;
		if (ret) {
			pr_info("%s      ret: %p\n", __func__, ret);
			if (IS_ERR(ret)) {
				atomic64_inc(&no_entry_cnt);
			}
		}
		else {
			pr_err("%s ret is NULL\n", __func__);
		}
	}
	return 0;
}

static int packet_drop_module_init(void)
{
    int ret;

    kp_ip_forward.pre_handler = ip_forward_pre_handler;
    ret = register_kprobe(&kp_ip_forward);
	if (ret < 0) {
        pr_err("register_kprobe kp_ip_forward failed\n");
        return -1;
    }
    else {
        pr_info("planted kprobe kp_ip_forward at %p\n", kp_ip_forward.addr);
    }

    krp_ip_route_input_slow.handler = ip_route_input_slow_ret_handler;
    ret = register_kretprobe(&krp_ip_route_input_slow);
	if (ret < 0) {
        pr_err("register_kretprobe krp_ip_route_input_slow failed\n");
        return -1;
    }
    else {
        pr_info("planted kretprobe krp_ip_route_input_slow at %p\n", krp_ip_route_input_slow.kp.addr);
    }

	krp_ip_route_output_flow.handler = ip_route_output_flow_ret_handler;
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