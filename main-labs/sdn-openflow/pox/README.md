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
| **BGP Announcement**           | A network example showing how to make basic BGP announcements between two routers. |
| **BGP Prefix Filtering**       | A network introducing to the use of prefix-lists, route-maps, and access-lists.    |
| **BGP Stub AS**                | Architecture of a stub network.                                                    |
| **BGP Stub AS Static**         | Configuration of a Stub AS with static routes.                                     |
| **BGP Multi-homed Stub**       | Configuration of a Multi-homed stub network with backup.                           |
| **BGP Multi-homed Stub Large** | A Multi-homed stub network running RIP.                                            |
| **BGP Multi-homed**            | Configuration of a Multi-homed network with backup and load sharing.               |
