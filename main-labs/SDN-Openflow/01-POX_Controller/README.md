# 01-POX_Controller

## Introduction

POX is a Python based SDN Controller, mainly used for teaching and research. It is based on two main layers:
* the Core layer: event, management, OpenFlow API, packet libraries,Python based API, etc.
* Component layer: stock and custom components.

But running POX by itself doesn't do much, POX functionality is provided by components. Components are specified on the commandline following any of the POX options.

An example of a POX component is forwarding.l2_learning: this component makes OpenFlow switches operate kind of like L2 learning switches.

## Lab

Now, we go to the hands on moment. We have created a POX component that listen to packetIn events and determine if they contain an IP packet.

### Test the implementation

Run the components A_listener and B_listener to test the implementation:

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

In h1 xterm:
```
ping 10.0.2.2
```

In s1 xterm:
```
ovs-ofctl dump-flows s1
```

You are able to execute a ping between the two hosts. But, if you dump the flow table of the switch to see the flow rules, there are not any rules. This is because the *l2_learning* is not enabled.

Launch ```kathara connect controller``` in the main terminal

Launch ```./home/pox/pox.py forwarding.l2_learning openflow.of_01 -port=6653``` in the root@controller

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal Warning
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switch
INFO:openflow.of_01:[e6-b1-b4-df-ec-42 1] connected
```

We do again the ping and the dump of the flow rules.

In h1 xterm:
```
ping 10.0.2.2
```

In s1 xterm:
```
ovs-ofctl dump-flows s1
```

You will obtain in s1 something like that:
```
cookie=0x0, duration=13.687s, table=0, n_packets=2, n_bytes=196, idle_timeout=10, hard_timeout=30, priority=65535,icmp,in_port=eth1,vlan_tci=0x0000,dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,nw_src=10.0.2.2,nw_dst=10.0.1.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:eth0
```

Close the root@controller with ```exit```

Close the lab with ```kathara lclean```