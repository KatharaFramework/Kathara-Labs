# 09-POX Routing

## Introduction

This is the last lab and it is the more complex. We advise you to see previous labs (to understand this better).

## Lab
In the controller, there are the following functionalities:
- a host and network discovery component
- a component that answers to ARP requests (assume that the gateway is at 10.0.0.1)
- a component that track the current occupation (in terms of number of flows) of each link
- a component that compute and install the “max throughput” path. The used algorithm is the Dijkstra's Algorithm: a shortest path search algorithm in a weighted graph, assigning a weight to each edge and finding the shortest path between a starting node and all other nodes.

![Network Scenario](../images/image3.png)

### Test the implementation

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Look at the controller xterm and **wait** until thw nx library is installed (about 3/4 minutes).

Launch ```kathara connect controller``` in the main terminal

Launch ```python3.9 /pox/pox.py openflow.of_01 -port=6653 component_ARP network_occupation host_discovery link_discovery max_throughput_routing``` in the root@controller

You will obtain: 
```
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
INFO:core:POX 0.7.0 (gar) is up.
INFO:openflow.of_01:[72-7b-f3-68-4e-4c 1] connected
INFO:openflow.of_01:[06-43-09-87-25-47 2] connected
INFO:openflow.of_01:[5a-84-07-ff-04-4b 4] connected
INFO:openflow.of_01:[02-a1-7d-b5-87-42 3] connected
```

Then, there are the discovered hosts:
```
host discovering
INFO:host_discovery:  ->  host 10.0.0.14 is connected to switch ([1], '72-7b-f3-68-4e-4c') through switch port 2
INFO:host_discovery:  ->  host 10.0.0.13 is connected to switch ([1], '72-7b-f3-68-4e-4c') through switch port 1
INFO:host_discovery:  ->  host 10.0.0.11 is connected to switch ([2], '06-43-09-87-25-47') through switch port 1
INFO:host_discovery:  ->  host 10.0.0.12 is connected to switch ([2], '06-43-09-87-25-47') through switch port 2
```

Then, there are the discovered links between the switches (as already seen in previous lab):
```
discovered new link: 1_4
{'name': '1_4', 'sid1': 1, 'sid2': 4, 'dpid1': '72-7b-f3-68-4e-4c', 'dpid2': '02-a1-7d-b5-87-42', 'port1': 4, 'port2': 2, 'flow': 0}
graph updated
discovered new link: 2_4
{'name': '2_4', 'sid1': 2, 'sid2': 4, 'dpid1': '06-43-09-87-25-47', 'dpid2': '02-a1-7d-b5-87-42', 'port1': 4, 'port2': 1, 'flow': 0}
graph updated
discovered new link: 1_3
{'name': '1_3', 'sid1': 1, 'sid2': 3, 'dpid1': '72-7b-f3-68-4e-4c', 'dpid2': '5a-84-07-ff-04-4b', 'port1': 3, 'port2': 2, 'flow': 0}
graph updated
discovered new link: 3_2
{'name': '3_2', 'sid1': 3, 'sid2': 2, 'dpid1': '5a-84-07-ff-04-4b', 'dpid2': '06-43-09-87-25-47', 'port1': 1, 'port2': 3, 'flow': 0}
graph updated
discovered new link: 4_2
{'name': '4_2', 'sid1': 4, 'sid2': 2, 'dpid1': '02-a1-7d-b5-87-42', 'dpid2': '06-43-09-87-25-47', 'port1': 1, 'port2': 4, 'flow': 0}
graph updated
discovered new link: 2_3
{'name': '2_3', 'sid1': 2, 'sid2': 3, 'dpid1': '06-43-09-87-25-47', 'dpid2': '5a-84-07-ff-04-4b', 'port1': 3, 'port2': 1, 'flow': 0}
graph updated
discovered new link: 3_1
{'name': '3_1', 'sid1': 3, 'sid2': 1, 'dpid1': '5a-84-07-ff-04-4b', 'dpid2': '72-7b-f3-68-4e-4c', 'port1': 2, 'port2': 3, 'flow': 0}
graph updated
discovered new link: 4_1
{'name': '4_1', 'sid1': 4, 'sid2': 1, 'dpid1': '02-a1-7d-b5-87-42', 'dpid2': '72-7b-f3-68-4e-4c', 'port1': 2, 'port2': 4, 'flow': 0}
graph updated
```

Every 30 seconds, there will be a printing with the flow of the different switches. The first one will be as follow:
```
switch [1] has 0 bytes and 0 flows
switch [3] has 0 bytes and 0 flows
switch [4] has 0 bytes and 0 flows
switch [2] has 0 bytes and 0 flows
```

Now, we try the routing algorithm. Go to h1 xterm and launch ```ping 10.0.0.13```. You will obtain:
```
INFO:max_throughput_routing:found path from 10.0.0.11 to 10.0.0.13 -> [(2, 4), (4, 1)]
  ->  link 2_4 has 1 flows
  ->  link 4_1 has 1 flows
INFO:max_throughput_routing:found path from 10.0.0.13 to 10.0.0.11 -> [(1, 3), (3, 2)]
  ->  link 1_3 has 1 flows
  ->  link 3_2 has 1 flows
```
The interesting point is that the path for the two flows (h1 to h3 and h3 to h1) are created to overcome the link overlapping, as the max throughput algorithm should do. You can try other ping to see that the behaviour is the same.

There will be another printing (every 30 seconds) with the flow of the different switches. The second one will be as follow:
```
switch [1] has 392 bytes and 2 flows
switch [2] has 392 bytes and 2 flows
switch [3] has 196 bytes and 1 flows
switch [4] has 196 bytes and 1 flows
```

Every 25 seconds, the flow table rules are removed, and the weight in the graph too.
```
INFO:max_throughput_routing:  ->  switch ([4], '02-a1-7d-b5-87-42') removed flow from 10.0.0.11 to 10.0.0.13
INFO:max_throughput_routing:  ->  switch ([3], '5a-84-07-ff-04-4b') removed flow from 10.0.0.13 to 10.0.0.11
INFO:max_throughput_routing:  ->  switch ([2], '06-43-09-87-25-47') removed flow from 10.0.0.11 to 10.0.0.13
INFO:max_throughput_routing:  ->  switch ([1], '72-7b-f3-68-4e-4c') removed flow from 10.0.0.11 to 10.0.0.13
INFO:max_throughput_routing:  ->  switch ([2], '06-43-09-87-25-47') removed flow from 10.0.0.13 to 10.0.0.11
INFO:max_throughput_routing:  ->  switch ([1], '72-7b-f3-68-4e-4c') removed flow from 10.0.0.13 to 10.0.0.11
```

There will be another printing with the flow of the different switches. It will be one be as follow:
```
switch [1] has 0 bytes and 0 flows
switch [3] has 0 bytes and 0 flows
switch [4] has 0 bytes and 0 flows
switch [2] has 0 bytes and 0 flows
```

The ARP handler component is doing the actions explained in the previous lab, but you have to de-comment the "print" in the Component_ARP.py

When you close the application, you obtain the disconnection from the switches:
```
INFO:openflow.of_01:[9e-8c-f4-ec-9c-4e 1] disconnected
INFO:openflow.of_01:[d2-37-cc-c7-70-41 2] disconnected
INFO:openflow.of_01:[86-94-e5-ad-df-42 3] disconnected
INFO:openflow.of_01:[b6-50-bc-90-a9-4d 4] disconnected
INFO:core:Down.
```

Close the root@controller with ```exit```

Close the lab with ```kathara lclean```
