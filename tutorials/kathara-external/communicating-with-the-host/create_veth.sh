#!/bin/bash

ip link add dev veth0 type veth peer name veth1

ip link set veth0 up
ip link set veth1 up

ip link add br0 type bridge

ip link set veth1 master br0

ip link set br0 up

iptables -A FORWARD -i br0 -o br0 -j ACCEPT