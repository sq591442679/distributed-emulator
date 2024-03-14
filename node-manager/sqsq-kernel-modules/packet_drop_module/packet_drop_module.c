#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/ftrace.h>
#include <linux/socket.h>
#include <linux/rcupdate.h>
#include <linux/init.h>
#include <linux/kallsyms.h>
#include <linux/linkage.h>
#include <linux/version.h>
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

static long long drop_cnt;

static struct kprobe kp_ip_forward = {
    .symbol_name = "ip_forward",
};



static int __kprobes handler_pre_ip_forward(struct kprobe *p, struct pt_regs *regs)
{
    struct sk_buff *skb = (struct sk_buff *)regs->di;

	if (ip_hdr(skb)->ttl <= 1) {
		drop_cnt++;
		// pr_info("current ttl drop_cnt: %lld\n", drop_cnt);
	}

    return 0;   
}

static int __init packet_drop_module_init(void)
{
    int ret;

	drop_cnt = 0ll;

    kp_ip_forward.pre_handler = handler_pre_ip_forward;
    ret = register_kprobe(&kp_ip_forward);
	if (ret < 0) {
        pr_err("register_kprobe ip_output failed\n");
    }
    else {
        pr_info("planted kprobe at %p\n", kp_ip_forward.addr);
    }

    return 0;
} 

static void __exit packet_drop_module_exit(void)
{
	pr_info("ttl exceed packet cnt: %lld\n", drop_cnt);
	unregister_kprobe(&kp_ip_forward);
    pr_info("%s	unregisterd kprobe\n", __func__);
}

module_init(packet_drop_module_init);
module_exit(packet_drop_module_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");