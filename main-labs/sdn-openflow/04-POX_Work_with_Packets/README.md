# 04-POX_Work_with_Packets

## Introduction
POX has a library for parsing and constructing packets. 
Most packets have some sort of a header and some sort of a payload.
Some of the packet types supported by POX are: ethernet, ARP, IPv4, ICMP, TCP, UDP, DHCP, DNS, LLDP, VLAN.

You can import the POX packet library with the command:
```import pox.lib.packet as pkt```

You can navigate the encapsulated packets in two ways:
* by using the payload attribute of the packet object
```
def parse_icmp (eth_packet):
    if eth_packet.type == pkt.IP_TYPE:
        ip_packet = eth_packet.payload
        if ip_packet.protocol == pkt.ICMP_PROTOCOL:
            icmp_packet = ip_packet.payload
```

* by using its find( ) method:
```
def handle_IP_packet (packet):
    ip = packet.find('ipv4')
        if ip is None:
            return
    print "Source IP:", ip.srcip
```

## Lab

We have created a POX component that listen to packetIn events and determine if they contain an IP packet.

### Test the implementation

Run the components A_listener and B_listener to test the implementation:

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Launch ```kathara connect controller``` in the main terminal

Launch ```./home/pox/pox.py Packet_check openflow.of_01 -port=6653``` in the root@controller

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal Warning, don't worry
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switch
INFO:openflow.of_01:[e6-b1-b4-df-ec-42 1] connected
```

In h1 xterm:
```
cd home

python3 sendARP.py 
#or
python3 sendIP.py 
```

In the root@controller terminal you will see:
```
# if you do python3 sendARP.py 
*** From Component: packet detected NOT IP!

# if you do python3 sendIP.py 
*** From Component: IP packet detected!
```

close the root@controller with ```exit```

close the lab with ```kathara lclean```

Inside the controller, there is another python3 script that does the same thing. Try it with the proper changes.