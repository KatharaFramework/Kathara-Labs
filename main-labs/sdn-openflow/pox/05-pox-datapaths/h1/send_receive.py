from scapy.all import *
from threading import Thread

def send_packet():
    frame = Ether(dst="11:22:33:44:55:66")/IP(src="10.0.1.1",dst="10.0.255.255")
    sendp(frame, iface="eth0")

def print_capture():
    sniff(count=1, iface="eth0", prn=lambda x: x.show(), timeout=5)

P1 = Thread(target = send_packet)
P2 = Thread(target = print_capture)

P2.start()
P1.start()
print("\n")
P2.join()
P1.join()
