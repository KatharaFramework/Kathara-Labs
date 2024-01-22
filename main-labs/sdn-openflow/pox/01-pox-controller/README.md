# 01-POX_Controller

## Introduction

This scenario contains an example of usage of a built-in POX component.

In particular, the scenario shows how to enable the `forwarding.l2_learning` component.

## Network Topology

![Network Scenario](../network_images/simple_network.png)

## Run the Network Scenario

To run the network scenario, open a terminal in the scenario directory and type:

```bash
kathara lstart 
```

To test the connectivity in the network, open the `h1` terminal and ping `h2`:

```
ping 10.0.2.2
```

You should be able to execute the ping, however, switch `s1` has its OpenFlow flows table empty:

```
ovs-ofctl dump-flows s1
```

This happens since the switch acts as a L2 learning switch by the default, but does not fill the table.

To enable the `forwarding.l2_learning` POX component and see the flow rules in the switch, go into the `controller`
terminal and type:
```
python3.9 /pox/pox.py forwarding.l2_learning openflow.of_01 -port=6653
``` 
**Note:** We installed `python3.9` on the `kathara/pox` image to improve compatibility with POX.

You will obtain something like:
```
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.
WARNING:version:Support for Python 3 is experimental.
INFO:core:POX 0.7.0 (gar) is up.
INFO:openflow.of_01:[16-6e-0d-ec-1e-41 1] connected
```

Now, retry to ping `h2` from `h1`:

```
ping 10.0.2.2
```

```
ovs-ofctl dump-flows s1
```

You will obtain in s1 something like that:

```
 cookie=0x0, duration=28.822s, table=0, n_packets=29, n_bytes=2842, idle_timeout=10, hard_timeout=30, priority=65535,icmp,in_port=eth0,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,nw_src=10.0.1.1,nw_dst=10.0.2.2,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:eth1
 cookie=0x0, duration=28.816s, table=0, n_packets=29, n_bytes=2842, idle_timeout=10, hard_timeout=30, priority=65535,icmp,in_port=eth1,vlan_tci=0x0000,dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,nw_src=10.0.2.2,nw_dst=10.0.1.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:eth0
 cookie=0x0, duration=7.718s, table=0, n_packets=1, n_bytes=60, idle_timeout=10, hard_timeout=30, priority=65535,arp,in_port=eth0,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,arp_spa=10.0.1.1,arp_tpa=10.0.2.2,arp_op=1 actions=output:eth1
 cookie=0x0, duration=7.714s, table=0, n_packets=1, n_bytes=60, idle_timeout=10, hard_timeout=30, priority=65535,arp,in_port=eth1,vlan_tci=0x0000,dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,arp_spa=10.0.2.2,arp_tpa=10.0.1.1,arp_op=2 actions=output:eth0
```

To undeploy the network scenario, open a terminal in the network scenario directory and type:
```bash
kathara lclean
```
