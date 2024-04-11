#!/bin/bash -er
docker build -t elb:latest .
echo "y" | docker image prune
echo "y" | docker builder prune