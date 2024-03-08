#!/bin/bash

LOG_FILE="/var/log/network_events.log"

log_event() {
    local event=$1
    local interface=$2
    local timestamp=$(date +"%Y-%m-%d %T")
    echo "$timestamp - $event: $interface" >> $LOG_FILE
}

ip monitor | while read -r line; do
    if [[ "$line" == *"state"* ]]; then
        interface=$(echo "$line" | awk '{print $NF}')
        state=$(echo "$line" | grep -oP "(?<=state )[^ ]+")

        log_event "Interface state changed to $state" "$interface"
    fi
done
