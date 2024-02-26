CONFIG_MODULE_SIG=n
KBUILD_FLAGS += -g -Wall
EXTRA_CFLAGS += -I$(PWD)/

obj-m += load_awareness_module.o

all:
	$(MAKE) -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	$(MAKE) -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean 
