# 05-POX_Datapaths

## Introduction

Controller to switch communication: this is performed by controller code which sends an OpenFlow message to a particular switch.
Switch to controller communication: messages show up in POX as events (for which you can write event handlers).

In POX, controller can communicate with a datapath in two ways:
* via a Connection object for that particular datapath: one connection object for each switch
* via an OpenFlow Nexus which is managing that datapath: one OpenFlow Nexus manages all connections

## Lab

We have created a POX component, called reflector, that: 
* it is a listener of packetIn events
* when a relevant event occurs, then the component extract the ethernet frame and swaps source and destination mac
*  after that, it sends the frame back in the dataplane through a packet out (see next slide), indicating to forward it out from the switch port from which it has been received

![Network Scenario](https://github.com/RicGobs/Kathara-Labs/blob/main/main-labs/sdn-openflow/network_images/network_image1.png)

### Test the implementation

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Launch ```kathara connect controller``` in the main terminal

Launch ```python3 /pox/pox.py reflector openflow.of_01 -port=6653``` in the root@controller

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

In h2 xterm, to see that no packet arrives:
```
# launch and leave it on
tcpdump -i eth0 
```

In h1 xterm:
```
cd home
python3 send_receive.py 
```

In the root@controller terminal you will see:
```
Received from (and sent back to): 00:00:00:00:00:01
The destination before was: 11:22:33:44:55:66
Port used: 1
```

You can see that the packet is reflected to h1 and h2 does not receive any packets.

Close the root@controller with ```exit```

Close the lab with ```kathara lclean```


Inside the controller there are also A_listener and B_listener component of the the 03-POX_Events lab. Try to launch all of them.