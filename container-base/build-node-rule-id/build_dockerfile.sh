#!/bin/bash -er
docker build -t node_rule_id:latest .
echo "y" | docker image prune
echo "y" | docker builder prune