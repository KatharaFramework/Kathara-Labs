from scapy.all import *

frame = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1, pdst="10.0.1.100", psrc="10.0.2.100")
sendp(frame, iface="eth0")
