# 05-Flowlet-Switching
Original network scenario can be found [here](https://github.com/nsg-ethz/p4-learning/tree/master/exercises/05-Flowlet_Switching).
There, you can find a detailed explanation about the scenario, and the exercise (here only the solution is provided).

## Network Scenario

This is the network scenario topology: 

![topology](images/multi_hop_topo.png)

The `s1` and `s6` switches implements a flowlet switching policy, sending traffic to all the nexthops for a destination,
leveraging the burstiness of TCP flows to achieve a better load balancing then ECMP. TCP flows tend to come in bursts 
(for instance because a flow needs to wait to get window space). 
Every time there is gap which is big enough (i.e., 50ms) between packets from the same flow, 
flowlet switching will rehash the flow to another path (by hashing an ID value together with the 5-tuple).

## Testing the scenario
1. To run the network scenario, open a terminal in the scenario directory and type: 
```bash
kathara lstart 
```

2. Open a terminal on one hosts and ping the others to verify reachability:
```bash
root@h1:/# ping 10.0.6.2 
```

3. If all the hosts can reach the others, open a tcpdump on the links towards `s1` and the other switches.

4. Ping between two hosts: you should see traffic in only 1 or 2 interfaces (due to the return path).
   Since all the ping packets have the same 5-tuple.

5. Do iperf between two hosts: you should also see traffic in 1 or 2 interfaces (due to the return path).
   Since all the packets belonging to the same flow have the same 5-tuple, and thus the hash always returns the same index.

6. Get a terminal in `h1`. Use the `send.py` script.

```bash
python3 send.py 10.0.6.2 1000 <sleep_time_between_packets>
```

This will send `tcp syn` packets with the same 5-tuple. You can play with the sleep time (third parameter). 
If you set it bigger than your gap, packets should change paths, if you set it smaller (set it quite smaller 
since the software model is not very precise) you will see all the packets cross the same interfaces.

