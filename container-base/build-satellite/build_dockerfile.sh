#!/bin/bash -er
docker build -t satellite_base:latest .
echo "y" | docker image prune
echo "y" | docker builder prune