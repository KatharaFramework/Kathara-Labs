# Exercise 3: Basic Switching

Welcome to Exercise 3! In this exercise, you'll explore a different way to use autocorrection. Unlike previous
exercises, you won't need to modify the provided lab. Instead, you’ll observe certain network behaviors and respond to
questions by creating files for each answer in the shared directory of the lab.

## Goal

The goal of this exercise is to enhance your understanding of Layer 2 switching by examining how communications impact
the MAC address tables of devices. You'll run the provided network scenario and answer the following questions.

### Question 1

After pinging `pc2` from `pc1` how many non-local MAC addresses are present in the MAC address table of `br0` on `s1`?

Create a file named `answer1.txt` in the `shared` directory of the lab containing only the number.

### Question 2

After a small period of time from the `ping` related to Question 1, which devices correspond to the MAC addresses listed
in the MAC address table of `br0` on `s1`?

Create a file named `answer2.txt` in the `shared` directory of the lab. List one device name per line.

### Question 3

Use `arping` from `pc1` to `pc2` (`100.0.0.2`). Through which interfaces on `s2` are the packets sent out?

Create a file named `answer3.txt` in the `shared` directory of the lab. Provide one interface name per line.

### Question 4

What is the destination MAC address of the ARP requests?

Create a file named `answer4.txt` in the `shared` directory of the lab. Provide one MAC address per line.

## Tips for Success

- Use the command `brctl showmacs <bridge_name>` to view the MAC address table of bridges.
- Use `tcpdump -tenni <eth_name>` to capture and analyze traffic on interfaces.
- Drawing out the network topology may help you visualize the connections and address ranges.

## Verifying Your Work

To ensure your network is set up correctly, you can use standard network troubleshooting tools like Wireshark, ping, and
traceroute.

When you're ready, use the `kathara-lab-checker` tool for automated validation of your exercise. Follow the installation
instructions provided in the [README](../README.md) under the exercises section.

To check the exercise, enter this directory and run the following command (ensure you activate the virtual
environment in every new shell session if you used it for the installation):

```bash
kathara-lab-checker -c autocorrection/correction.json --lab lab --no-cache --report-type none
```

If you run the tool before starting the exercise, it should report that only four tests have failed (the ones related to
the questions). The passing tests ensure that the lab setup is correct. Since no modifications to the lab are required
for this exercise, the checks verify that everything remains unaltered.
