/**
 * mainly utilizes ftrace to modify the execution flow, 
 * i.e., only execute our sqsq_fib_select_multipath and no longer execute original fib_select_multipath in kernel
 * refers to R3tr074's brokepkg in https://github.com/R3tr074/brokepkg
 */

#include "my_ftrace.h"

static asmlinkage void (*orig_fib_select_multipath)(struct fib_result *res, struct flowi4 *fl4, int hash);

asmlinkage void sqsq_fib_select_multipath(struct fib_result *res, const struct flowi4 *fl4)
{
	// pr_info("%s %p %p\n", __func__, (void *)res, (void*)fl4);

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