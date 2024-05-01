#!/bin/bash -er
docker build -t node_table:latest .
echo "y" | docker image prune
echo "y" | docker builder prune