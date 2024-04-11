/**
 * monitor NF_INET_PRE_ROUTING and NF_INET_LOCAL_OUT for input network traffic,
 * NF_INET_POST_ROUTING for output network traffic
 */

#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netdevice.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/netfilter_bridge.h>
#include <linux/ip.h>
#include <linux/timer.h>
#include <linux/rwlock.h>
#include <linux/atomic.h>
#include <linux/types.h>
#include <net/net_namespace.h>

#define TIMER_INTERVAL 1000

const char interface_names[4][5] = {"eth1", "eth2", "eth3", "eth4"};

static struct nf_hook_ops pre_routing_nfho, local_output_nfho, post_routing_nfho;
static struct nf_hook_ops *nfhos[3] = {&pre_routing_nfho, &local_output_nfho, &post_routing_nfho};

static struct timer_list timer;

static atomic_t pre_routing_packets = ATOMIC_INIT(0);
static atomic_t local_output_packets = ATOMIC_INIT(0);
static atomic_t post_routing_packets = ATOMIC_INIT(0);

static unsigned int input_rate = 0, output_rate = 0;  	// I and O in eq.1 of ELB paper, unit: pkts, not bytes
static unsigned int queue_capacity = 0;					// Q_l in eq.1, unit: pkts
module_param(queue_capacity, uint, S_IRUGO);
MODULE_PARM_DESC(queue_capacity, "queue capacity, unit: pkts");
static double delta_d = 0.0f;							// delta_d un eq.1

// static DEFINE_RWLOCK(pre_routing_bytes_lock);

static void timer_callback(struct timer_list *unused)
{
	struct net *net;
	int i;

	for_each_net(net) {
		if (net != &init_net) {
			for (i = 0; i < 4; ++i) {
				struct net_device *dev = dev_get_by_name(net, interface_names[i]);
				if (dev != NULL) {
					
				}
			}
		}
	}

    input_rate = atomic_read(&pre_routing_packets) + atomic_read(&local_output_packets);
    output_rate = atomic_read(&post_routing_packets);

	delta_d = 

    atomic_set(&pre_routing_packets, 0);
    atomic_set(&local_output_packets, 0);
    atomic_set(&post_routing_packets, 0);

    mod_timer(&timer, jiffies + msecs_to_jiffies(TIMER_INTERVAL_MS));
}

static unsigned int pre_routing_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_inc(&pre_routing_packets);

    return NF_ACCEPT;
}

static unsigned int local_output_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_inc(&local_output_packets);

    return NF_ACCEPT;
}

static unsigned int post_routing_hook(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    atomic_inc(&post_routing_packets);

    return NF_ACCEPT;
}

static int __init elb_init(void)
{
    unsigned int hooknums[3] = {NF_INET_PRE_ROUTING, NF_INET_LOCAL_OUT, NF_INET_POST_ROUTING};
    unsigned int (*hooks[3])(void *, struct sk_buff *, const struct nf_hook_state *) = {
        &pre_routing_hook, &local_output_hook, &post_routing_hook
    };
    int i; 
	struct net *net;

    timer_setup(&timer, timer_callback, 0);
    mod_timer(&timer, jiffies + msecs_to_jiffies(TIMER_INTERVAL_MS * 1000));

    for (i = 0; i < 3; ++i) {
        struct nf_hook_ops *nfho = nfhos[i];
        nfho->hook = hooks[i];
        nfho->hooknum = hooknums[i];
        nfho->pf = PF_INET;
        nfho->priority = NF_IP_PRI_FIRST;
        for_each_net(net) {
			if (net != &init_net) {
				nf_register_net_hook(net, nfho);
			}
		}
        
    }
    
    return 0;
}

static void __exit elb_exit(void)
{
	struct net *net;
    int i;
    for (i = 0; i < 3; ++i) {
		struct nf_hook_ops *nfho = nfhos[i];
        for_each_net(net) {
			if (net != &init_net) {
				nf_unregister_net_hook(net, nfho);
			}
		}
    }
}

module_init(elb_init);
module_exit(elb_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");
