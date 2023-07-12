# Capture Packets using Wireshark GUI

This tutorial explain how to capture packets of a collision domain using Wireshark.

Thanks to [nopid](https://github.com/nopid) and [whatever4711](https://github.com/whatever4711) for suggesting this brilliant solution! :rocket:

## Let's start!
Let's consider the simple network scenario in the [lab](lab) directory, that is composed by two devices, namely 
`pc1` and `pc2`

Suppose you want to capture packets between the two devices `pc1` and `pc2` on the collision domain `A`.

This is the `.startup` file of `pc1`:
```bash
ip address add 100.0.0.1/24 dev eth0
```
And this is the `.startup` file of `pc2`:
```bash
ip address add 100.0.0.2/24 dev eth0
```
To do so you have to add a `wireshark` device to the network scenario (in the [lab.conf](lab/lab.conf) file) 
connected to the collision domain to sniff.

```txt
pc1[0]=A
pc2[0]=A

wireshark[0]=A
wireshark[bridged]=true
wireshark[image]="lscr.io/linuxserver/wireshark"
```

Note that to capture packets on more than one collision domain, you only need to connect the `wireshark` device on desired collision domains. 

The `wireshark` device uses the `lscr.io/linuxserver/wireshark` image, which exposes a Wireshark GUI accessible using 
a web browser. To access the GUI you need to connect on the bridged interface of the device on port 3000.

You can connect to the GUI following these steps:

1. Go into the `wireshark` device and find the bridged interface IP address:
    ```bash
    root@wireshark:/# ip address
    ...
    37: eth1@if38: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1500 qdisc noqueue state UP 
        link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff
        inet 172.17.0.2/16 brd 172.17.255.255 scope global eth1
       valid_lft forever preferred_lft forever
    ```
2. Access the GUI through a web browser using the following URL (`http://<ip_bridged>:3000`):
   - `http://172.17.0.2:3000/`
   By default, the user/pass is abc/abc. If you change your password or want to login manually to the GUI session for 
   any reason use the following link: `http://172.17.0.2:3000/?login=true`

3. You can select the interface connected to the collision domain to sniff (e.g., `eth0`).
   ![Wireshark Interfaces](images/wireshark-tutorial-1.png)

4. Now, you can see packets exchanged on that collision domain between the devices.
   ![Wireshark Packets](images/wireshark-tutorial-2.png)

