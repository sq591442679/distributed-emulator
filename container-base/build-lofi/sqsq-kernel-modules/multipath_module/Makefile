CONFIG_MODULE_SIG=n
KBUILD_FLAGS += -g -Wall
EXTRA_CFLAGS += -I$(PWD)/

obj-m += multipath_module.o

KERNEL_SRC := /lib/modules/$(shell uname -r)/build

# VPATH := $(PWD)

# ccflags-y := -I$(src) -I$(KERNEL_SRC)/include

all:
	$(MAKE) -C $(KERNEL_SRC) M=$(PWD) modules

clean:
	$(MAKE) -C $(KERNEL_SRC) M=$(PWD) clean 
