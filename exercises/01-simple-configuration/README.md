# Exercise 1: Simple Configuration

In this exercise, you will configure a Kathará network device on your own. Don't worry—an example configuration is
provided for reference!

The task is to add a new device to the network scenario found in the [lab](lab) directory and properly configure the
network topology, device interfaces, and their IP addresses.
By the end of the exercise, both devices should be able to `ping` each other on all interfaces.

## Goal

The goal of this exercise is to deepen your understanding of network configuration by adding and setting up a new device
in a pre-existing Kathará network scenario. You will be responsible for configuring the network topology, interfaces,
and IP addresses for the new device so that it can seamlessly communicate with the existing device.

By the end of this exercise, both the new and pre-configured devices should be able to successfully `ping` each other on
all interfaces, demonstrating correct network connectivity and configuration. An example configuration is provided to
guide you through the process, but the main objective is to independently apply what you've learned to set up a
functioning network environment.

## Requirements

The network setup consists of the following:

- Two devices: `pc1` and `pc2`.
- `pc1` and `pc2` are connected through collision domain `B`.
- `pc2` has two network interfaces:
    - The first interface is connected to `pc1` via collision domain `B`.
    - The second interface is connected to collision domain `C`.
- Devices in collision domain `A` use the address range `100.1.0.0/24`.
- Devices in collision domain `B` use the address range `100.2.0.0/24`.
- Devices in collision domain `C` use the address range `100.3.0.0/24`.
- The final octet of each device's IP address corresponds to its device number (e.g., `.1` for `pc1`).
- The routing table of `pc1` contains the prefix directly connected plus the `100.3.0.0/24`.
- The routing table of `pc2` contains the prefix directly connected plus the `100.1.0.0/24`.
- `pc1` should be able to ping all of `pc2`'s interfaces successfully.
- `pc2` should be able to ping all of `pc1`'s interfaces successfully.

## Tips for Success

- Use the configuration of `pc1` as a reference for setting up `pc2`.
- It might be helpful to draw out the network topology on paper to visualize the connections and address ranges.

## Verifying Your Work

To verify your configuration, you can use the `kathara-lab-checker` tool to automatically check the exercise. To install
the tool, follow the instructions provided by the [README](../README.md) of the exercises section.

To check the exercise, use the following command (ensure you activate the virtual environment in every new shell
session, if you used it for the installation):

```bash
kathara-lab-checker -c solution/add_one_router_solution.json --lab lab --no-cache
```

If you run the tool before starting the exercise (as recommended), you should see that only 6 out of 17 tests passed.

Use the error explanations provided to guide your next steps.

The tool also generates a `.xlsx` report in the lab directory, which consists of three sheets:

1. **Summary**: Provides an overall summary of the results.
2. **All**: Displays the results for each test.
3. **Failed**: Lists only the failed test results.

Now you're ready to dive into the exercise!



