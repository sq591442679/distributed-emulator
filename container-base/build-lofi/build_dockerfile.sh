#!/bin/bash -er
docker build -t lofi:latest .
echo "y" | docker image prune
echo "y" | docker builder prune