#!/bin/bash

set -xe

IMAGE_TAG=${1:-v0.1}

docker run --rm \
    --volume data:/usr/src/etljob/data \
    etljob:$IMAGE_TAG