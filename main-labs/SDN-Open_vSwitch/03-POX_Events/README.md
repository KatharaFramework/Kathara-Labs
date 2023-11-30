# 02-POX_Events

Event handling in POX fits into the publish/subscribe paradigm.
Events in POX are all instances of subclasses of revent.Event.

OpenFlow related events have the following three attributes:
* connection: Connection to the relevant switch (e.g., which sent the message this event corresponds to)
* dpid: Datapath ID of relevant switch (use dpid_to_str( )
to format it for display)
* ofp: OpenFlow message object that caused this event

ConnectionUp event is fired in response to the establishment of a new control channel with a switch.

ConnectionDown event is fired when a connection to a switch has been
terminated.

PortStatus events are raised when the controller receives an OpenFlow port-status message from a switch.

FlowRemoved events are raised when the controller receives an OpenFlow flow-removed message from a switch.

Statistics events are raised when the controller receives an OpenFlow statistics reply message from a switch.

PacketIn event is fired when the controller receives an OpenFlow packet-in message.

ErrorIn event is fired when the controller receives an OpenFlow error message.


Now, we go to the hands on moment:
* we have created two POX components
* the component A is a listener of packetIn events: whenever a packetIn event occurs, the component A prints a message on the display publishes an event named pktInSeen
* the component B is a listener of pktInSeen events: whenever a pktInSeen event occurs, the component B prints the message “A has seen an OFP packetIn” on the screen.

Test the implementation:




 
```from pox.core import core```
