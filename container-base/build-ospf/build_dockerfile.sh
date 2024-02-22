#!/bin/bash -er
docker build -t ospf:latest .
echo "y" | docker image prune
echo "y" | docker builder prune