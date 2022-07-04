#!/bin/bash

set -u
set -e

TOP_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

cd "${TOP_DIR}" || exit 1

source .env

docker build \
    -t "${GITLAB_CI_IMAGE}:${GITLAB_CI_TAG}" \
    --build-arg GITLAB_IMAGE="${GITLAB_IMAGE}" \
    --build-arg GITLAB_TAG="${GITLAB_TAG}" \
    --no-cache \
    "${TOP_DIR}"
