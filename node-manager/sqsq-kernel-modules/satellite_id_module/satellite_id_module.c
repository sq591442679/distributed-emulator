/**
 * receive satellite id from user space
 * and set the corresponding member of include/net/namespace.h
 */

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/kprobes.h>
#include <linux/socket.h>
#include <linux/netlink.h>
#include <linux/netdevice.h>
#include <linux/types.h>

#include <net/net_namespace.h>
#include <net/netlink.h>
#include <net/sock.h>
#include <net/sch_generic.h>

#define NETLINK_SATELLITE_ID	29
#define SATELLITE_ID_PID		369369

static void netlink_receive_satellite_id(struct sk_buff *skb)
{
	if (skb->len >= nlmsg_total_size(0)) {
		struct nlmsghdr *hdr = nlmsg_hdr(skb);
		__u32 satellite_id = 0;

		if (nlmsg_len(hdr) != sizeof(satellite_id)) {
			pr_err("%s: netlink payload error\n", __func__);
			return;
		}

		satellite_id = *((__u32 *)NLMSG_DATA(hdr));
		pr_info("%s satellite_id: %u\n", __func__, satellite_id);

		sock_net(skb->sk)->satellite_id = satellite_id;

		pr_info("%pI4    %s\n", &satellite_id, __func__);
	}
	else {
		pr_err("%s skb error!\n", __func__);
	}
}


static void init_netlink_sockets(void)
{
	struct net *net;
	for_each_net(net) {
		if (net != &init_net) {
			struct netlink_kernel_cfg cfg;
			struct sock* nl_sk;

			memset(&cfg, 0, sizeof(struct netlink_kernel_cfg));

			cfg.groups = 1;
			cfg.input = netlink_receive_satellite_id;

			nl_sk = netlink_kernel_create(net, NETLINK_SATELLITE_ID, &cfg);

			if (nl_sk == NULL) {
				pr_err("%s netlink_kernel_create failed\n", __func__);
			}
			else {
				pr_info("%s netlink_kernel_create succeed\n", __func__);
			}

			net->satellite_id_sock = nl_sk;		
		}	
	}
}

static void release_netlink_sockets(void)
{
	struct net *net;
	for_each_net(net) {
		if (net != &init_net) {
			netlink_kernel_release(net->satellite_id_sock);
			net->satellite_id_sock = NULL;	
		}
	}
}

static int satellite_id_module_init(void)
{
	init_netlink_sockets();
	return 0;
}

static void satellite_id_module_exit(void)
{
	release_netlink_sockets();
}

module_init(satellite_id_module_init);
module_exit(satellite_id_module_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");