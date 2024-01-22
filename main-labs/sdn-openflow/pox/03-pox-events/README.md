# 03-POX_Events

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

![Network Scenario](https://github.com/RicGobs/Kathara-Labs/blob/main/main-labs/sdn-openflow/network_images/network_image1.png)

### Test the implementation

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Launch ```kathara connect controller``` in the main terminal

Launch ```/pox/pox.py A_listener B_listener openflow.of_01 -port=6653``` in the root@controller

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al.

# Result for each ping
*** From Component_A: packetIn captured!
*** From Component_B: A has seen an OFP packetIn!

# normal warning, don't worry
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
INFO:core:POX 0.7.0 (gar) is up.
```

close the root@controller with ```exit```

close the lab with ```kathara lclean```