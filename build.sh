#!/bin/bash

set -xe

IMAGE_TAG=${1:-v0.1}

docker build \
    --no-cache \
    -t etljob:$IMAGE_TAG .