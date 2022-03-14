# 02-Repeater
Original network scenario can be found [here](https://github.com/nsg-ethz/p4-learning/tree/master/exercises/02-Repeater).
There, you can find a detailed explanation about the scenario, and the exercise (here only the solution is provided).

## Network Scenario
This is the network scenario topology: 

![topology](images/topology.png)

It is composed by three devices: two host `h1` and `h2`, and one switch `s1`. 
This is a very simple example in which `s1` act as a repeater. 
In other words, when a packet enters `port 1` it has to be leave from `port 2` and vice versa.

## Testing the scenario
1. To run the network scenario, open a terminal in the scenario directory and type: 
```bash
kathara lstart 
```

2. For testing the P4 program, open a terminal on `h2` and run receive.py: 
```bash
python3 receive.py
```

3. Then, open a terminal on `h1` and run receive.py: 
```bash
python3 send.py 10.0.0.2 "Hello H2"
```

You will see an output like this on `h2`: 

```bash 
Packet Received:
###[ Ethernet ]### 
  dst       = 06:07:08:09:0a:0b
  src       = 00:01:02:03:04:05
  type      = IPv4
###[ IP ]### 
     version   = 4
     ihl       = 5
     tos       = 0x0
     len       = 28
     id        = 1
     flags     = 
     frag      = 0
     ttl       = 64
     proto     = hopopt
     chksum    = 0x66df
     src       = 10.0.0.1
     dst       = 10.0.0.2
     \options   \
###[ Raw ]### 
        load      = 'Hello H2'
```