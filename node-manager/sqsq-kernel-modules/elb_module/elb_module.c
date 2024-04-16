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

static int __init elb_module_init(void)
{
    return 0;
}

static void __exit elb_module_exit(void)
{

}

module_init(elb_module_init);
module_exit(elb_module_exit);

