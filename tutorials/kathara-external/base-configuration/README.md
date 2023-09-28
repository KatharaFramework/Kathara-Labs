# Kathará External - Base Configuration (Linux Only)

This tutorial shows a simple example on how to correctly configure Kathará External to allow a Kathará device to send
packets through a host interface.

## Configuration
Let's consider a very simple network scenario composed by a single device. 

```text
pc1[0]="A"
pc1[image]="kathara/base"
```

To connect device interfaces to host physical interfaces, we need to create a `lab.ext` file.  

The file has the following syntax:
```text
<collision_domain> <physical_interface>
```
Each line requires two parameters: 
- the `collision_domain` to attach to a host physical interface;
- the host `physical_interface`.

Now, let's connect `pc1` to a host interface. To do so, we need to write the following `lab.ext`:
```text
A <physical_interface>
```

where `<physical_interface>` is the name of the physical interface on your host (e.g., `enp0s31f6`). 

Before running the lab, let's configure the IP address of `pc1` in the `pc1.startup` file:
```bash 
ip address add 10.0.0.1/24 dev eth0
```

Now we only need to run the network scenario. We need root privileges to use external, so open a terminal in the 
network scenario directory and type: 
```text
sudo kathara lstart
```

## Testing
To test that everything works as expected, we can ping any address in `10.0.0.0/24` while dumping on the host interface:

1. Start a dump on the host physical interface (e.g., enp0s31f6):
    ```bash
    tcpdump -tenni enp0s31f6
    ```
2. Connect to `pc1` using the connect command:
    ```bash
    kathara connect pc1
    ```
3. Now, ping `10.0.0.2` from `pc1`:
    ```bash
    ping 10.0.0.2
    ```

On the interface host you should see packets from `pc1`:
```text
sudo tcpdump -tenni enp0s31f6 | grep 10.0.0.1
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on enp0s31f6, link-type EN10MB (Ethernet), snapshot length 262144 bytes
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
be:05:0e:3e:49:1b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 10.0.0.2 tell 10.0.0.1, length 46
```

## Resources
You can find a ready-to-run example in the [lab](lab) directory. You only need to replace `<physical_interface>` with 
the name of one of your host interfaces in the `lab.ext` file.
