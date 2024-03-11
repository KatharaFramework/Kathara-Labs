# 06-POX Link Discovery

## Introduction

POX contains classes and constants corresponding to elements of the OpenFlow protocol. Some examples are:

* ofp_packet_out, sending packets from the switch
* ofp_flow_mod, flow table modification
* ofp_stats_request, requesting statistics from switches

## Lab

We have created a POX discovery application that:

* allows the controller to know the network topology (switches and link between them)
* Switches are discovered by handling connection up events
* Links are discovered by exploiting the mechanism show in the figure

![Network Scenario](../images/image2.png)

### Test the implementation

To run the network scenario, open a terminal in the scenario directory and type:
```bash
kathara lstart 
```

Launch  in the root@controller:
```
python3.9 /pox/pox.py link_discovery_solution1 openflow.of_01 -port=6653
```

You will obtain:

```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal Warning, don't worry
WARNING:version:Support for Python 3 is experimental.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switches
INFO:openflow.of_01:[9e-8c-f4-ec-9c-4e 1] connected
Connection Up: 9e-8c-f4-ec-9c-4e, 1
INFO:openflow.of_01:[d2-37-cc-c7-70-41 2] connected
Connection Up: d2-37-cc-c7-70-41, 2
INFO:openflow.of_01:[86-94-e5-ad-df-42 3] connected
Connection Up: 86-94-e5-ad-df-42, 3
INFO:openflow.of_01:[b6-50-bc-90-a9-4d 4] connected
Connection Up: b6-50-bc-90-a9-4d, 4
```

Remember that **ConnectionUp event** is fired in response to the establishment of a new control channel with a switch.

Then, there are the discovered links between the switches:

```
discovered new link: 1_2
{'name': '1_2', 'sid1': 1, 'sid2': 2, 'dpid1': '9e-8c-f4-ec-9c-4e', 'dpid2': 'd2-37-cc-c7-70-41', 'port1': 1, 'port2': 1}
discovered new link: 2_1
{'name': '2_1', 'sid1': 2, 'sid2': 1, 'dpid1': 'd2-37-cc-c7-70-41', 'dpid2': '9e-8c-f4-ec-9c-4e', 'port1': 1, 'port2': 1}
discovered new link: 3_2
{'name': '3_2', 'sid1': 3, 'sid2': 2, 'dpid1': '86-94-e5-ad-df-42', 'dpid2': 'd2-37-cc-c7-70-41', 'port1': 1, 'port2': 2}
discovered new link: 1_4
{'name': '1_4', 'sid1': 1, 'sid2': 4, 'dpid1': '9e-8c-f4-ec-9c-4e', 'dpid2': 'b6-50-bc-90-a9-4d', 'port1': 2, 'port2': 2}
discovered new link: 2_3
{'name': '2_3', 'sid1': 2, 'sid2': 3, 'dpid1': 'd2-37-cc-c7-70-41', 'dpid2': '86-94-e5-ad-df-42', 'port1': 2, 'port2': 1}
discovered new link: 4_3
{'name': '4_3', 'sid1': 4, 'sid2': 3, 'dpid1': 'b6-50-bc-90-a9-4d', 'dpid2': '86-94-e5-ad-df-42', 'port1': 1, 'port2': 2}
discovered new link: 4_1
{'name': '4_1', 'sid1': 4, 'sid2': 1, 'dpid1': 'b6-50-bc-90-a9-4d', 'dpid2': '9e-8c-f4-ec-9c-4e', 'port1': 2, 'port2': 2}
discovered new link: 3_4
{'name': '3_4', 'sid1': 3, 'sid2': 4, 'dpid1': '86-94-e5-ad-df-42', 'dpid2': 'b6-50-bc-90-a9-4d', 'port1': 2, 'port2': 1}
```

When you close the application, you obtain the disconnection from the switches:

```
INFO:openflow.of_01:[9e-8c-f4-ec-9c-4e 1] disconnected
INFO:openflow.of_01:[d2-37-cc-c7-70-41 2] disconnected
INFO:openflow.of_01:[86-94-e5-ad-df-42 3] disconnected
INFO:openflow.of_01:[b6-50-bc-90-a9-4d 4] disconnected
INFO:core:Down.
```

To undeploy the network scenario, open a terminal in the network scenario directory and type:
```bash
kathara lclean
```

In the controller there is another possible solution, if you want to try it, repeat the tutorial with: 
```
python3.9 /pox/pox.py link_discovery_solution2 openflow.of_01 -port=6653
```