# Exercise 4: Subnetting in a Single LAN Scenario

Welcome to Exercise 4! In this exercise, you will dive deeper into the concepts of subnetting, broadcast addresses, and
routing tables within a simple LAN network. You’ll need to apply subnetting rules to answer several questions about the
network setup.

## Goal

The goal of this exercise is to reinforce your understanding of IP subnetting by exploring the allocation of IP
addresses, the calculation of broadcast addresses, and how routing tables operate in a subnetted network. You will
analyze the network shown in the diagram and answer the following questions.

### Scenario Description

You have a network with the base IP `200.100.50.0/24`. This network includes `router1`, which is connected
to `router2` via a point-to-point link `10.0.0.0/30`. The two PCs (`pc1` and `pc2`) are connected to `router1` and
belong to the same subnet.

In this scenario, you'll need to work with the following subnets:

- **LAN A**: `200.100.50.0/24`
- **LAN B (point-to-point link)** between `router1` and `router2`: `10.0.0.0/30`

### Question 1

How many usable IP addresses are available for hosts on the subnet `200.100.50.0/24`? (Exclude the network address and
the broadcast address.)

- Create a file named `answer1.txt` in the `shared` directory of the lab.
- The file should contain only the number of usable IP addresses.

### Question 2

Suppose the network `200.100.50.0/24` is split into two smaller subnets by using a `/25` prefix length. What are the
**network address** and **broadcast address** of each of the two subnets?

- Create a file named `answer2.txt` in the `shared` directory of the lab.
- Write the network address and broadcast address for both subnets (one subnet per line).

```
<network address> <broadcast_address>
<network address> <broadcast_address>
```

### Question 3

Using the subnet `200.100.50.0/24`, what is the **broadcast address** for this network?

- Create a file named `answer3.txt` in the `shared` directory of the lab.
- Provide the broadcast address for the entire `/24` network.

### Question 4

How would the network `200.100.50.0/24` change if you further subnet it using a `/26` prefix length? How many usable
host addresses would you get per subnet, and what would be the **network** and **broadcast addresses** of the first
two `/26` subnets?

- Create a file named `answer4.txt` in the `shared` directory of the lab.
- Write the network address and broadcast address for the first two `/26` subnets, along with the number of usable host
  addresses in each.

```
<network address> <broadcast_address> <usable_host>
<network address> <broadcast_address> <usable_host>
```

### Question 5

Examine the point-to-point link between `router1` and `router2` (`10.0.0.0/30`). What are the **network address** and
**broadcast address** of this `/30` subnet?

- Create a file named `answer5.txt` in the `shared` directory of the lab.
- Provide the network address and broadcast address for the `/30` subnet (one address for each line, following the
  specified order).

### **Question 6**

Modify the network `200.100.50.0/24` by subnetting it into two `/25` subnets. Configure `router1` to route between these
two subnets and the point-to-point link with `router2`.

The new network requirements are as follows:

- `eth0` of `router1` is connected to LAN `A` and assigned the **first usable address** from the first `/25` subnet.
- `eth1` of `router1` is connected to LAN `B` and assigned the **first usable address** from the second `/25` subnet.
- `eth2` of `router1` is connected to LAN `C`, retaining the address `10.0.0.2/30`.
- `eth0` of `pc1` is connected to LAN `A` and assigned the **second usable address** from the first `/25` subnet.
- `eth0` of `pc2` is connected to LAN `B` and assigned the **second usable address** from the second `/25` subnet.
- `router1` route packets between the two `\25` subnets and the point-to-point link.

Update the network scenario located in the [lab](lab) directory to meet the new requirements. Modify the `lab.conf` and
the required startup files to ensure that all interfaces and routing configurations are properly adjusted
for `router1`, `pc1`, and `pc2`.

## Tips for Success

- Use subnetting rules to calculate the number of available host IP addresses for each subnet.
- Recall that the network address is the first address in the range, and the broadcast address is the last.

## Subnetting Refresher

- A `/24` subnet provides 256 addresses (including the network and broadcast address).
- A `/25` subnet halves the address space into two subnets, each with 128 addresses.
- A `/30` subnet, typically used for point-to-point links, provides 4 addresses (2 usable for hosts).

## Verifying Your Work

You can verify subnetting calculations by using `subnet calculators` tools. To check the routing
tables, use commands such as `ip route`.

When you are ready, you can use the `kathara-lab-checker` tool to automatically verify your exercise. Follow the
installation instructions provided in the [README](../README.md) section.

To check your exercise, run the following command:

```bash
kathara-lab-checker -c autocorrection/single_lan_subnetting.json --lab lab --no-cache --skip-report
```
