# 06-POX_Discovery

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

![Network Scenario](https://github.com/RicGobs/Kathara-Labs/blob/main/main-labs/sdn-openflow/network_images/network_image2.png)

### Test the implementation

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Launch ```kathara connect controller``` in the main terminal

Launch ```/pox/pox.py link_discovery_solution1 openflow.of_01 -port=6653``` in the root@controller

You will obtain:

```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal Warning, don't worry
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
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

Close the lab with ```kathara lclean```

In the controller there is another possible solution, if you want to try it, repeat the tutorial with: 
```
/pox/pox.py link_discovery_solution2 openflow.of_01 -port=6653
```