# 03 - POX Events

## Introduction
Event handling in POX fits into the publish/subscribe paradigm. 

OpenFlow related events have the following three attributes:
* **connection**: Connection to the relevant switch (e.g., which sent the message this event corresponds to)
* **dpid**: Datapath ID of relevant switch (use dpid_to_str( ) to format it for display)
* **ofp**: OpenFlow message object that caused this event

The possible OpenFlow Events are:
* **ConnectionUp event** is fired in response to the establishment of a new control channel with a switch.
* **ConnectionDown event** is fired when a connection to a switch has been
terminated.
* **PortStatus events** are raised when the controller receives an OpenFlow port-status message from a switch.
* **FlowRemoved events** are raised when the controller receives an OpenFlow flow-removed message from a switch.
* **Statistics events** are raised when the controller receives an OpenFlow statistics reply message from a switch.
* **PacketIn event** is fired when the controller receives an OpenFlow packet-in message.
* **ErrorIn event** is fired when the controller receives an OpenFlow error message.


## Lab

We have created two POX components:
* the component A_listener is a listener of packetIn events: whenever a packetIn event occurs, the component A prints a message on the display publishes an event named pktInSeen
* the component B_listener is a listener of pktInSeen events: whenever a pktInSeen event occurs, the component B prints the message “A has seen an OFP packetIn” on the screen.

![Network Scenario](../images/image1.png)

### Test the implementation

To run the network scenario, open a terminal in the scenario directory and type:
```bash
kathara lstart 
```

Launch in the root@controller:
```
python3.9 /pox/pox.py A_listener B_listener openflow.of_01 -port=6653
```

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# normal warning, don't worry
WARNING:version:Support for Python 3 is experimental.
INFO:core:POX 0.7.0 (gar) is up.
```

Launch ```ping 10.0.2.2``` in the `h1` terminal.

In the root@controller you will obtain: 
```
# Result for each ping
*** From Component_A: packetIn captured!
*** From Component_B: A has seen an OFP packetIn!
```

To undeploy the network scenario, open a terminal in the network scenario directory and type:
```bash
kathara lclean
```