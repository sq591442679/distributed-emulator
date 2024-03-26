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

static struct kretprobe krp_fib_table_lookup = {
    .kp.symbol_name = "fib_table_lookup",
    .maxactive = NR_CPUS,
    .data_size = sizeof(struct my_data),
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

static int fib_table_lookup_entry_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
    struct my_data *data = (struct my_data *)ri->data;
    struct fib_table *tb = (struct fib_table *)regs->di;
    struct flowi4 *flp = (struct flowi4 *)regs->si;
    struct fib_result *res = (struct fib_result *)regs->dx;
    
    // pr_info("%s.daddr: %pI4\n", __func__, &(flp->daddr));
    // pr_info("%s.res: %p\n", __func__, res);
    // pr_info("%s: type:%d\n", __func__, res->type);

    if (!data) {
        pr_err("%s: !data\n", __func__);
        return -ENOMEM;
    }

    data->flp = flp;
    data->res = res;
    data->tb = tb;
    
    // if (res->type == RTN_UNICAST) {
    //     pr_info("UNICAST\n");
    //     data->res = res;
    // }
    // else {
    //     data->res = NULL;
    // }

    return 0;
}

static int fib_table_lookup_ret_handler(struct kretprobe_instance *ri, struct pt_regs *regs)
{
    struct my_data *data = (struct my_data *)ri->data;
    struct fib_table *tb;
    struct flowi4 *flp;
    struct fib_result *res;

    if (!data || !data->res || !data->flp || !data->tb) {
        pr_err("%s: %p %p %p %p\n", __func__, data, data->res, data->flp, data->tb);
        return 0;
    }

    tb = data->tb;
    flp = data->flp;
    res = data->res;

    // if (tb->tb_id == MAIN_TABLE_ID && flp->daddr == htonl((__be32)dst_ip)) {
    //     pr_info("%s: %pI4\n", __func__, &(flp->daddr));
    // }

    if ((int)regs_return_value(regs) != 0) {
        // pr_info("%s: %pI4 %pI4\n", __func__, &(flp->daddr), &dst_ip);
        if (tb->tb_id == MAIN_TABLE_ID && flp->daddr == htonl((__be32)dst_ip)) {
            pr_info("%s: %pI4, ret:%d\n", __func__, &(flp->daddr), (int)regs_return_value(regs));
            atomic64_inc(&no_entry_cnt);
        }   
    }

    return 0;
}

static int __init packet_drop_module_init(void)
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

    krp_fib_table_lookup.handler = fib_table_lookup_ret_handler;
    krp_fib_table_lookup.entry_handler = fib_table_lookup_entry_handler;
    ret = register_kretprobe(&krp_fib_table_lookup);
	if (ret < 0) {
        pr_err("register_kretprobe krp_fib_table_lookup failed\n");
        return -1;
    }
    else {
        pr_info("planted kretprobe krp_fib_table_lookup at %p\n", krp_fib_table_lookup.kp.addr);
    }

    return 0;
} 

static void __exit packet_drop_module_exit(void)
{
	pr_info("ttl exceed packet cnt: %lld\n", atomic64_read(&ttl_drop_cnt));
	unregister_kprobe(&kp_ip_forward);
    pr_info("%s	unregisterd kprobe\n", __func__);

    pr_info("no entry packet cnt: %lld\n", atomic64_read(&no_entry_cnt));
	unregister_kretprobe(&krp_fib_table_lookup);
    pr_info("%s	unregisterd kretprobe\n", __func__);
}

module_init(packet_drop_module_init);
module_exit(packet_drop_module_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");