# POX

## Introduction

[POX](https://github.com/noxrepo/pox) is an OpenFlow controller written in Python.

POX provides a framework for communicating with SDN switches using either the OpenFlow or OVSDB protocol. Developers can
use POX to create an SDN controller using the Python programming language.

POX can be immediately used as a basic SDN controller by using the stock components that come bundled with it.
However, developers may create a more complex SDN controller by creating new POX components.

A detailed description of POX and the available components can be
found [here](https://noxrepo.github.io/pox-doc/html/#components-in-pox).

## Available Scenarios 

| Name                           | Description                                                                        |
|--------------------------------|------------------------------------------------------------------------------------|
| **POX Controller**             | Simple example about the `forwarding.l2_learning` component.                       |
| **POX Core Object**            | Introduction to pox components.                                                    |
| **POX Events**                 | Introduction to OpenFlow events management.                                        |
| **POX Work with Packets**      | Introduction to parsing and packets creation.                                      |
| **POX Datapaths**              | Communication between controller and switch.                                       |
| **POX Link Discovery**         | Implementation of a pox component that discover the links of the network.          |
| **POX Host Discovery**         | Implementation of a pox component that discover the links of the network.          |
| **POX ARP Handler**            | Implementation of a pox component that answers to ARP requests of the hosts.       |
| **POX Routing**                | Final lab that implements a routing function in the network.                       |

## Acknowledgements
The scenarios refer to the **Programmable Network** Course of La Sapienza University of Rome, held by Professor **Marco Polverini**.
