# Fixed Delay
This simple example shows how to add a fixed delay on a device interface. 

## Configuring the lab
For this example we consider the following `lab.conf` file:

```shell
pc1[0]="A"
pc1[image]="kathara/base"

r1[0]="A"
r1[1]="B"
r1[image]="kathara/base"

pc2[0]="B"
pc2[image]="kathara/base"
```

Our goal is to add a fixed delay on `eth0` of `r1`.

We start configuring `pc1`. To do so, we create a `pc1.startup` file with the following content: 
```shell
ip address add 100.0.0.2/24 dev eth0

ip route add default via 100.0.0.1 dev eth0
```

Then we do the same thing for the `pc2.startup` file:
```shell
ip address add 200.0.0.2/24 dev eth0

ip route add default via 200.0.0.1 dev eth0
```

Now we are ready to configure `r1`, writing its `r1.startup` file:
```shell
ip address add 100.0.0.1/24 dev eth0
ip address add 200.0.0.1/24 dev eth1

tc qdisc add dev eth0 root netem delay 10ms
```

The last line tells to `tc` to add a queuing discipline (*qdisc*) on `eth0` to add `10ms` of delay on each packet
traversing the interface.
The queuing discipline uses the `netem` module, which is used for network emulation, 
allowing you to introduce various types of network impairments to simulate real-world network conditions.

To test the effectiveness of the command let's ping from `pc1` to `pc2`:

![img.png](images/ping-fixed-delay.png)

As it is possible to notice, the delay is about `10ms` for each packet!

You can find the complete configuration of devices in the [lab](lab) directory.

For more details on the `tc` command, see the [man-pages](https://man7.org/linux/man-pages/man8/tc.8.html).
