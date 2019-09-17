#!/usr/bin/env bash

apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq \
  tzdata \
  python3-pip \
  python3-dev \
  iputils-ping \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

pip3 install boto3
pip3 install PyYAML
pip3 install subprocess32 gradescope-utils
