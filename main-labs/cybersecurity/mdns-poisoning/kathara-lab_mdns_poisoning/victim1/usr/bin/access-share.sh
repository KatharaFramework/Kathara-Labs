#!/bin/sh

for i in $(seq 1 10000); do
    timeout 5 smbclient //srv1.local/share -U valerio%iloveyou
    sleep 5
done