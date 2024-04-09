/**
 * monitor NF_INET_PRE_ROUTING and NF_INET_LOCAL_OUT for input network traffic,
 * NF_INET_POST_ROUTING for output network traffic
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netdevice.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/timer.h>
#include <linux/rwlock.h>
#include <linux/atomic.h>
#include <linux/types.h>

static struct nf_hook_ops pre_routing_nfho, local_output_nfho, post_routing_nfho;
static struct nf_hook_ops *nfhos[3] = {&pre_routing_nfho, &local_output_nfho, &post_routing_nfho};

static struct timer_list timer;

static atomic_t pre_routing_bytes = ATOMIC_INIT(0);
static atomic_t local_output_bytes = ATOMIC_INIT(0);
static atomic_t post_routing_bytes = ATOMIC_INIT(0);
static atomic_t received_packets = ATOMIC_INIT(0);

static unsigned long long input_rate = 0, output_rate = 0;  // I and O in eq.1 of ELB paper

static DEFINE_RWLOCK(pre_routing_bytes_lock);

static void timer_callback(unsigned long para)
{
    
}

static unsigned int pre_routing_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_add(skb->len, &pre_routing_bytes);

    atomic_inc(&received_packets);

    return NF_ACCEPT;
}

static unsigned int local_output_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_add(skb->len, &local_output_bytes);

    atomic_inc(&received_packets);

    return NF_ACCEPT;
}

static unsigned int post_routing_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_add(skb->len, &post_routing_bytes);
    return NF_ACCEPT;
}

static int __init elb_init(void)
{
    unsigned int hooknums[3] = {NF_INET_PRE_ROUTING, NF_INET_LOCAL_OUT, NF_INET_POST_ROUTING};
    unsigned int (*hooks[3])(void *, struct sk_buff *, const struct nf_hook_state *) = {
        &pre_routing_hook, &local_output_hook, &post_routing_hook
    };
    int i; 

    timer_setup(&timer, timer_callback, 0);

    for (i = 0; i < 3; ++i) {
        struct nf_hook_ops *nfho = nfhos[i];
        nfho->hook = hooks[i];
        nfho->hooknum = hooknums[i];
        nfho->pf = PF_INET;
        nfho->priority = NF_IP_PRI_FIRST;
        nf_register_hook(nfho);
    }
    
    return 0;
}

static void __exit elb_exit(void)
{
    int i;
    for (i = 0; i < 3; ++i) {
        nf_unregister_hook(nfhos[i]);
    }
}

module_init(elb_init);
module_exit(elb_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");
