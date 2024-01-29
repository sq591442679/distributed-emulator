#!/bin/bash

# mount tmpfs filesystem
mount -t tmpfs none /run
mount -t tmpfs none /run/lock

systemctl enable frr
systemctl start frr

# exec other commands
exec "$@"

