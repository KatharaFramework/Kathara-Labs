# 01-Reflector
Original network scenario can be found [here](https://github.com/nsg-ethz/p4-learning/tree/master/exercises/01-Reflector).
In that page, you can find a detailed explanation about the scenario, and the exercise (here only the solution is provided).

## Network Scenario
It is composed by two devices: one host `h1` and one switch `s1`. 
This is a very simple example in which `s1` bounces back packets received on an interface. 

## Testing the scenario
To run the network scenario, open a terminal in the scenario directory and type: 
```bash
kathara lstart 
```

For testing the P4 program, open a terminal on `h1` and type: 
```bash
python3 send_receive.py 
```

You will see an output like this: 

```bash
root@h1:/# python3 send_receive.py 
Press the return key to send a packet:
Sending on interface eth0 to 10.0.0.2

[!] A packet was reflected from the switch: 
[!] Info: 00:01:02:03:04:05 -> 4a:ca:38:cf:c4:32

[!] A packet was reflected from the switch: 
[!] Info: 00:01:02:03:04:05 -> 4a:ca:38:cf:c4:32
```