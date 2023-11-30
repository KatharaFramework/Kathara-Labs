# 01-POX_Controller

POX is a Python based SDN Controller, mainly used for teaching and research. It is based on two main layers:
* the Core layer: event, management, OpenFlow API, packet libraries,Python based API, etc.
* Component layer: stock and custom components.

But running POX by itself doesn't do much, POX functionality is provided by components. Components are specified on the commandline following any of the POX options.
An example of a POX component is forwarding.l2_learning: this component makes OpenFlow switches operate kind of like L2 learning switches. To run this component:
'./pox.py forwarding.l2_learning'

To see the what this component does:
* Run the Kathara lab provided: 'kathara lstart'
* the command l2_learning is already installed in the controller.startup
* you are able to execute a ping between the two hosts
