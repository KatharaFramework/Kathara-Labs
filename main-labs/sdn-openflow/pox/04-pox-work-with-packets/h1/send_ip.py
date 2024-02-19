from scapy.all import *

frame = Ether(dst="11:22:33:44:55:66")/IP(src="10.0.1.1",dst="10.0.255.255")
sendp(frame, iface="eth0")
