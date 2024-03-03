/**
 * mainly utilizes ftrace to modify the execution flow, 
 * i.e., only execute our sqsq_fib_select_multipath and no longer execute original fib_select_multipath in kernel
 * refers to R3tr074's brokepkg in https://github.com/R3tr074/brokepkg
 */

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

#include <net/ip_fib.h>
#include <net/nexthop.h>

struct ftrace_hook {
  const char *name;
  void *function;
  void *original;

  unsigned long address;
  struct ftrace_ops ops;
};

static asmlinkage void (*orig_fib_select_multipath)(struct fib_result *res, struct flowi4 *fl4, int hash);

int fh_resolve_hook_address(struct ftrace_hook *hook) {
#if LINUX_VERSION_CODE >= KERNEL_VERSION(5, 7, 0)
	static struct kprobe kp = {.symbol_name = "kallsyms_lookup_name"};
	typedef unsigned long (*kallsyms_lookup_name_t)(const char *name);
	kallsyms_lookup_name_t kallsyms_lookup_name;
	register_kprobe(&kp);
	kallsyms_lookup_name = (kallsyms_lookup_name_t)kp.addr;
	unregister_kprobe(&kp);
#endif
	hook->address = kallsyms_lookup_name(hook->name);

	if (!hook->address) {
		pr_debug("brokepkg: unresolved symbol: %s\n", hook->name);
		return -ENOENT;
	}

	*((unsigned long *)hook->original) = hook->address;

	return 0;
}

void notrace fh_ftrace_thunk(unsigned long ip, unsigned long parent_ip,
                             struct ftrace_ops *ops,
                             struct ftrace_regs *fregs) {
	struct pt_regs *regs = ftrace_get_regs(fregs);
	struct ftrace_hook *hook = container_of(ops, struct ftrace_hook, ops);

	if (!within_module(parent_ip, THIS_MODULE))
		regs->ip = (unsigned long)hook->function;
}

int fh_install_hook(struct ftrace_hook *hook) {
	int err;
	err = fh_resolve_hook_address(hook);
	if (err) return err;

	hook->ops.func = fh_ftrace_thunk;
	hook->ops.flags = FTRACE_OPS_FL_SAVE_REGS | FTRACE_OPS_FL_RECURSION |
						FTRACE_OPS_FL_IPMODIFY | FTRACE_OPS_FL_RCU;

	err = ftrace_set_filter_ip(&hook->ops, hook->address, 0, 0);
	if (err) {
		pr_err("brokepkg: ftrace_set_filter_ip() failed: %d\n", err);
		return err;
	}

	err = register_ftrace_function(&hook->ops);
	if (err) {
		pr_err("brokepkg: register_ftrace_function() failed: %d\n", err);
		return err;
	}

	return 0;
}

void fh_remove_hook(struct ftrace_hook *hook) {
	int err;
	err = unregister_ftrace_function(&hook->ops);
	if (err) {
		pr_err("brokepkg: unregister_ftrace_function() failed: %d\n", err);
	}

	err = ftrace_set_filter_ip(&hook->ops, hook->address, 1, 0);
	if (err) {
		pr_err("brokepkg: ftrace_set_filter_ip() failed: %d\n", err);
	}
}

asmlinkage void sqsq_fib_select_multipath(struct fib_result *res, const struct flowi4 *fl4)
{
	pr_info("%s %p %p\n", __func__, (void *)res, (void*)fl4);

	if (likely(res->fi->nh)) {
		struct nh_info *nhi;
		struct nexthop *nh;

		if (!res->fi->nh->is_group) {
			nh = res->fi->nh;
		}
		else {
			struct nh_group *nhg = rcu_dereference(res->fi->nh->nh_grp);
			int i = 0;
			struct nh_grp_entry *min_weight_nhge = NULL;
			for (i = 0; i < nhg->num_nh; ++i) {
				struct nh_grp_entry *nhge = &nhg->nh_entries[i];
				if (i == 0) {
					min_weight_nhge = nhge;
				}
				else {
					struct nh_info *info = rcu_dereference(nhge->nh->nh_info);
					if (nhge->weight < min_weight_nhge->weight && info->fib_nhc.nhc_oif != fl4->__fl_common.flowic_iif) {
						min_weight_nhge = nhge;
					}
				}
			}
			if (min_weight_nhge) {
				nh = min_weight_nhge->nh;
			}
			else {
				nh = NULL;
			}
		}

		if (nh == NULL) {
			pr_info("%s  nh == NULL!!!!!\n", __func__);	
		}

		nhi = rcu_dereference(nh->nh_info);
		res->nhc = &nhi->fib_nhc;
		return;
	}

	else {
		pr_err("%s res->fi->nh is NULL\n",  __func__);
	}
}

static struct ftrace_hook fh = {
	.name = "fib_select_multipath",
	.function = sqsq_fib_select_multipath,
	.original = &orig_fib_select_multipath
};

static int __init multipath_module_init(void)
{
    
	fh_install_hook(&fh);

	pr_info("multiath_module running\n");

    return 0;
}

static void __exit multipath_module_exit(void)
{
	fh_remove_hook(&fh);
}

module_init(multipath_module_init);
module_exit(multipath_module_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("sqsq");