1. how to install:
1.1 enter folder packet_drop_module/
1.2 'make' command
1.3 'sudo insmod packet_drop_module.ko dst_ip=xxx' command

2. how to get result
2.1 'rmmod packet_drop_module' command
2.2 'dmesg' command
2.2 can see ttl exceed packet cnt: ...

NOTE: only record packet drop due to ttl exceed; recording of packet drop due to no routing table entry hasn't correctly implemented