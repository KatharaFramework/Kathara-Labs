#!/bin/bash -e
CA=$1


krillc add --ca $CA
krillc repo request \
    --ca $CA > /tmp/publisher_request.xml
krillc pubserver publishers add \
    --publisher $CA \
    --request /tmp/publisher_request.xml > /tmp/repository_response.xml
krillc repo configure \
    --ca $CA \
    --format text \
    --response /tmp/repository_response.xml
krillc parents request \
    --ca $CA > /tmp/myid.xml
krillc children add \
    --ca ta \
    --child $CA \
    --asn "AS0-65535" \
    --ipv4 "0.0.0.0/0" \
    --request /tmp/myid.xml > /tmp/parent_response.xml
krillc parents add \
    --ca $CA \
    --parent ta \
    --response /tmp/parent_response.xml
