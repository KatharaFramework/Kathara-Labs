#!/bin/sh

SERVER_VIP=$1
REQUEST_COUNT=100

if [ -z "$SERVER_VIP" ]; then
   echo "Please specify the VIP of a web server as argument"
   exit 1
fi

function get_reply_md5() {
   wget http://$1/ -O - 2>/dev/null | md5sum
}

# Get md5sums of each server's page
route add default gw 10.0.0.1
SERVER1_MD5=$(get_reply_md5 100.0.0.1)
SERVER2_MD5=$(get_reply_md5 100.0.0.2)
SERVER3_MD5=$(get_reply_md5 100.0.0.3)
route del default

for ((i=1; i<=$REQUEST_COUNT; i++)); do
   REPLY_MD5=$(get_reply_md5 $SERVER_VIP)
   [ "$REPLY_MD5" = "$SERVER1_MD5" ] && echo "replies received from server 1"
   [ "$REPLY_MD5" = "$SERVER2_MD5" ] && echo "replies received from server 2"
   [ "$REPLY_MD5" = "$SERVER3_MD5" ] && echo "replies received from server 3"
done | sort | uniq -c

