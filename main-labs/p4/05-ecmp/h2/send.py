#!/usr/bin/env python
import argparse
import sys
import random
import struct

from scapy.all import sendp, get_if_hwaddr
from scapy.all import Ether, IP, UDP, TCP

def main():
    if len(sys.argv)<3:
        print('pass 2 arguments: <destination> <number_of_random_packets>')
        exit(1)

    addr = sys.argv[1]
    iface = "eth0"

    print("sending on interface %s to %s" % (iface, str(addr)))

    pkt = Ether(src=get_if_hwaddr(iface), dst='00:00:00:06:02:00')
    pkt = pkt /IP(dst=addr) / TCP(dport=random.randint(5000,60000), sport=random.randint(49152,65535))
    sendp(pkt, iface=iface, verbose=True, loop=int(sys.argv[2]), inter=0.5)

if __name__ == '__main__':
    main()
