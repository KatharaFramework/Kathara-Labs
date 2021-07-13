FROM kathara/base

ARG DEBIAN_FRONTEND="noninteractive"
RUN apt update && \
    apt install -y python3-pip

RUN python3 -m pip install scapy

RUN apt clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/