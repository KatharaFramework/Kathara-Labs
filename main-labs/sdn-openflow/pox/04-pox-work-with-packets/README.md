# 04-POX Work with Packets

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

* by using its `find()` method:
```
def handle_IP_packet (packet):
    ip = packet.find('ipv4')
        if ip is None:
            return
    print "Source IP:", ip.srcip
```

## Lab

We have created a POX component that listen to packetIn events and determine if they contain an IP packet.

![Network Scenario](../images/image1.png)


### Test the implementation

To run the network scenario, open a terminal in the scenario directory and type:
```bash
kathara lstart 
```

Launch in the `root@controller`:
```
python3.9 /pox/pox.py PacketCheck openflow.of_01 -port=6653
```

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal Warning, don't worry
WARNING:version:Support for Python 3 is experimental.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switch
INFO:openflow.of_01:[e6-b1-b4-df-ec-42 1] connected
```

In `h1` terminal:
```
python3 send_arp.py 
#or
python3 send_ip.py 
```

In the `root@controller` terminal you will see:
```
# if you do python3 send_arp.py 
*** From Component: packet detected NOT IP!

# if you do python3 send_ip.py 
*** From Component: IP packet detected!
```

To undeploy the network scenario, open a terminal in the network scenario directory and type:
```bash
kathara lclean
```

Inside the controller, there is the script IPL.py that implements the same application. Try it with the proper changes.
