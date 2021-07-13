#!/usr/bin/env python
import sys
import socket
import random
import time
from threading import Thread, Event
from scapy.all import *

def send_packet(iface):
    input("Press the return key to send a packet:")
    print("Sending on interface %s\n" % (iface))
    pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff:ff')
    pkt = pkt
    sendp(pkt, iface=iface, verbose=False)

def main():
    iface = "eth0"

    while True:
        send_packet(iface)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
