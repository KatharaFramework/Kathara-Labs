# Kathará External - VLAN Configuration (Linux Only)

This tutorial shows a simple example on how to correctly configure Kathará External using VLANs.

## Configuration
Let's consider a very simple network scenario composed by a single device. 

```text
pc1[0]="A"
pc1[image]="kathara/base"
```

To connect device interfaces to host physical interfaces, we need to create a `lab.ext` file.  

The file has the following syntax:
```text
<collision_domain> <physical_interface>.<vlan_id>
```
Each line requires two parameters: 
- the `collision_domain` to attach to a host physical interface;
- the host `physical_interface`;
- the `vlan_id` to use for tagging packets after exiting the host physical interface;

Now, let's connect `pc1` to a host interface, assigning 10 as VLAN ID. 
To do so, we need to write the following `lab.ext`:
```text
A <physical_interface>.10
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

On the interface host you should see packets from `pc1` tagged with `vlan 10`:
```text
sudo tcpdump -tenni enp0s31f6 | grep 10.0.0.1
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on enp0s31f6, link-type EN10MB (Ethernet), snapshot length 262144 bytes
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
9e:58:73:e4:4d:4a > ff:ff:ff:ff:ff:ff, ethertype 802.1Q (0x8100), length 64: vlan 10, p 0, ethertype ARP (0x0806), Request who-has 10.0.0.2 tell 10.0.0.1, length 46
```

## Resources
You can find a ready-to-run example in the [lab](lab) directory. You only need to replace `<physical_interface>` with 
the name of one of your host interfaces in the `lab.ext` file. 