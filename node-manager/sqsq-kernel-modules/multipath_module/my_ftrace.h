#ifndef MY_FTRACE_H
#define MY_FTRACE_H

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

int fh_resolve_hook_address(struct ftrace_hook *hook);
void notrace fh_ftrace_thunk(unsigned long ip, unsigned long parent_ip,
                             struct ftrace_ops *ops,
                             struct ftrace_regs *fregs);
int fh_install_hook(struct ftrace_hook *hook);
void fh_remove_hook(struct ftrace_hook *hook);

#endif