# Exercise 2: Add one router

Welcome to Exercise 2! This exercise builds on what you learned
in [Exercise 1: Simple Configuration](../01-simple-configuration), where you
familiarized yourself with basic networking concepts and the autocorrection tool. Now, we'll take it a step further by
introducing an additional router and host to a more complex network topology.

Your goal in this exercise is to extend the provided ([lab](lab)) by adding and configuring a new router and a
host in the network scenario. This will require properly setting up the device interfaces and assigning appropriate IP
addresses and routing tables.

By the end of the exercise, all the hosts should be able to `ping` each other.

## Goal

The goal is simple but essential: add a new router and host to an existing network and ensure hosts connectivity.
The scenario already contains several pre-configured devices, and you will need to modify the network to include the new
elements while ensuring that all hosts can reach each other.

## Requirements

The network setup consists of the following:

- Three hosts: `pc1`, `pc2`, `pc3`.
- Three routers: `r1`, `r2`, `r3`.
- `pc1` and `r1` are connected through collision domain `A`.
- `pc2` and `r2` are connected through collision domain `C`.
- `pc3` and `r3` are connected through collision domain `D`.
- `r1` and `r2` are connected through collision domain `B`.
- `r1` and `r3` are connected through collision domain `E`.
- `r2` and `r3` are connected through collision domain `F`.
- The final octet of each router's IP address corresponds to its device number (e.g., `.1` for `r1`).
- The final octet of each host's IP address corresponds is equal to `2`.
- Devices in collision domain `A` use the address range `100.1.0.0/24`.
- Devices in collision domain `C` use the address range `100.2.0.0/24`.
- Devices in collision domain `D` use the address range `100.3.0.0/24`.
- Devices in collision domain `B` use the address range `10.0.0.0/30`.
- Devices in collision domain `E` use the address range `10.0.0.4/24`.
- Devices in collision domain `F` use the address range `10.0.0.8/24`.
- The routing table of each router only contains the prefixes directly connected plus the other `100.X.0.0/24` prefixes.
- The routing table of each device contains the prefix directly connected plus a default route pointing to its router.
- All the hosts should be able to `ping` each other.

## Task Outline

1. Add a new router to the topology in the lab directory and properly configure it.
2. Add a new host that connects to the new router.
3. Ensure all IP addresses are correctly assigned based on the topology guidelines.
4. Update routing tables where necessary to allow for full network communication.
5. Verify connectivity by making sure that each host can successfully ping any other host in the network.

## Tips for Success

- Use the configurations of the pre-existing devices as references for setting up your new router and host.
- It might be helpful to draw out the network topology on paper to visualize the connections and address ranges.
- Pay close attention to the IP addressing scheme and make sure it follows the guidelines provided.

## Verifying Your Work

To verify your configuration, you can use the `kathara-lab-checker` tool to automatically check the exercise. To install
the tool, follow the instructions provided by the [README](../README.md) of the exercises section.

To check the exercise, use the following command (ensure you activate the virtual environment in every new shell
session, if you used it for the installation):

```bash
kathara-lab-checker -c solution/add_one_router_solution.json --lab lab --no-cache
```



