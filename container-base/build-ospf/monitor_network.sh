#!/bin/bash

LOG_FILE="/var/log/network_events.log"

log_interface() {
    local event=$1
    local interface=$2
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S.%3N")
    echo "$timestamp - $event: $interface" >> $LOG_FILE
}

log_routing_table() {
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S.%3N")
    echo "$timestamp - routing table changed" >> $LOG_FILE
}

ip monitor | while read -r line; do
    if [[ "$line" == *"state"* ]]; then
        interface=$(echo "$line" | awk -F '@if' '{print $1}' | awk '{print $NF}')
        state=$(echo "$line" | grep -oP "(?<=state )[^ ]+")

        log_interface "Interface state changed to $state" "$interface"
    elif [[ "$line" == *"zebra"* ]]; then
        log_routing_table
    fi
done
