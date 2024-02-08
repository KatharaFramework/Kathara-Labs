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
| **POX Core Object**           | A network example showing how to make basic BGP announcements between two routers. |
| **POX Events**       | A network introducing to the use of prefix-lists, route-maps, and access-lists.    |
| **POX Work with Packets**                | Architecture of a stub network.                                                    |
| **POX Datapaths**         | Configuration of a Stub AS with static routes.                                     |
| **POX Link Discovery**       | Configuration of a Multi-homed stub network with backup.                           |
| **POX Host Discovery** | A Multi-homed stub network running RIP.                                            |
| **POX ARP Handler**            | Configuration of a Multi-homed network with backup and load sharing.               |
| **POX Routing**            | Configuration of a Multi-homed network with backup and load sharing.               |
