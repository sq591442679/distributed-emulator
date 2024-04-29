#include <netlink/socket.h>
#include <netlink/netlink.h>
#include <netlink/msg.h>
#include <netlink/route/link.h>
#include <netlink/route/tc.h>
#include <netlink/route/qdisc.h>
#include <netlink/utils.h>
#include <netlink/cache.h>
#include <unistd.h>
#include <stdio.h>
#include <math.h>

#define NETLINK_SATELLITE_ID	29

u_int32_t satellite_id;     

/**
 * argv[1]: uint32	satellite_id
 */
int main(int argc, char const *argv[])
{
    struct nl_sock *sk;
    int ret, i;
    struct nl_msg *delta_msg = nlmsg_alloc();
    struct nlmsghdr *hdr;

    if (argc != 2) {
        perror("parameter invalid\n");
        return -1;
    }

    satellite_id = (u_int32_t)atoi(argv[1]);

	printf("received parameter: %u\n", satellite_id);

    sk = nl_socket_alloc();

    nl_socket_disable_seq_check(sk);

    nl_socket_set_local_port(sk, 0);	// automatically allocate pid

    nl_connect(sk, NETLINK_SATELLITE_ID);

    // send satellite_id to kernel
    hdr = nlmsg_put(delta_msg, 0, NL_AUTO_SEQ, NETLINK_SATELLITE_ID, sizeof(satellite_id), NLM_F_CREATE);
    if (hdr == NULL) {
        perror("nlmsg_put failed\n");
    }
    memcpy(nlmsg_data(hdr), &satellite_id, sizeof(satellite_id));
    ret = nl_send_auto(sk, delta_msg);
    if (ret < 0) {
        perror("nl_send_auto failed\n");
		return ret;
    }
    // printf("netlink data len:%d\n", nlmsg_datalen(hdr));
    printf("sent satellite_id:%u\n", satellite_id);

	nlmsg_free(delta_msg);
	nl_socket_free(sk);

    return 0;
}
