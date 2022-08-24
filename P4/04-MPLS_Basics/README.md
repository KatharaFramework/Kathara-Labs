# 05-MPLS_Basics
Original network scenario can be found [here](https://github.com/nsg-ethz/p4-learning/tree/master/exercises/04-MPLS).
There, you can find a detailed explanation about the scenario, and the exercise (here only the solution is provided).

This network scenario has been adapted by Marco Vignaga (University of Padua).

## Network Scenario

This is the network scenario topology: 

![topology](images/mpls.png)

This topology implements a mock MPLS architecture. In this mock architecture, 
we have a single label for each packet that allows to enable communication
between `h1`, `h2`, and `h3`.

## Testing the scenario
1. To run the network scenario, open a terminal in the scenario directory and type: 
```bash
kathara lstart 
```

2. Open a terminal on `h1` and ping `h2`, and `h3` and check that they reply correctly:
```bash
root@h1:/# ping -c 4 10.7.2.2
PING 10.7.2.2 (10.7.2.2) 56(84) bytes of data.
64 bytes from 10.7.2.2: icmp_seq=1 ttl=63 time=15.3 ms
64 bytes from 10.7.2.2: icmp_seq=2 ttl=63 time=6.94 ms
64 bytes from 10.7.2.2: icmp_seq=3 ttl=63 time=11.3 ms
64 bytes from 10.7.2.2: icmp_seq=4 ttl=63 time=8.15 ms

--- 10.7.2.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 10ms
rtt min/avg/max/mdev = 6.936/10.424/15.296/3.236 ms
root@h1:/# ping -c 4 10.7.3.2
PING 10.7.3.2 (10.7.3.2) 56(84) bytes of data.
64 bytes from 10.7.3.2: icmp_seq=1 ttl=63 time=40.9 ms
64 bytes from 10.7.3.2: icmp_seq=2 ttl=63 time=12.0 ms
64 bytes from 10.7.3.2: icmp_seq=3 ttl=63 time=19.2 ms
64 bytes from 10.7.3.2: icmp_seq=4 ttl=63 time=11.5 ms

--- 10.7.3.2 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 17ms
rtt min/avg/max/mdev = 11.544/20.908/40.876/11.920 ms
```

3. Open a tcpdump on `eth1` of `s1`.

4. Ping from `h1` to `h2`: you should see MPLS packets on `s1`.
```bash
root@s1:/# tcpdump -i eth1
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth1, link-type EN10MB (Ethernet), capture size 262144 bytes
12:31:47.951169 MPLS (label 2, exp 0, ttl 254) (label 282624, exp 0, ttl 84) (label 612068, exp 0, ttl 0) (label 262168, exp 7, ttl 47) (label 40976, exp 0, [S], ttl 2)
	0x0000:  0a07 0202 0800 5b1b 0004 0010 3319 e962  ......[.....3..b
	0x0010:  0000 0000 b381 0e00 0000 0000 1011 1213  ................
	0x0020:  1415 1617 1819 1a1b 1c1d 1e1f 2021 2223  .............!"#
	0x0030:  2425 2627 2829 2a2b 2c2d 2e2f 3031 3233  $%&'()*+,-./0123
	0x0040:  3435 3637                                4567
12:31:47.954544 MPLS (label 1, exp 0, ttl 251) (label 282624, exp 0, ttl 84) (label 422016, exp 0, ttl 0) (label 262175, exp 6, ttl 149) (label 41072, exp 1, ttl 2) (label 40976, exp 0, [S], ttl 2)
	0x0000:  0000 631b 0004 0010 3319 e962 0000 0000  ..c.....3..b....
	0x0010:  b381 0e00 0000 0000 1011 1213 1415 1617  ................
	0x0020:  1819 1a1b 1c1d 1e1f 2021 2223 2425 2627  .........!"#$%&'
	0x0030:  2829 2a2b 2c2d 2e2f 3031 3233 3435 3637  ()*+,-./01234567
```

5. Stop the tcpdump and open it on `eth2` of `s1`.

6. Ping from `h1` to `h3`: you should see MPLS packets on `s1`.
```bash
root@s1:/# tcpdump -tenni eth2
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth2, link-type EN10MB (Ethernet), capture size 262144 bytes
00:00:0a:07:03:02 > 00:00:00:03:01:00, ethertype MPLS unicast (0x8847), length 102: MPLS (label 3, exp 0, ttl 254) (label 282624, exp 0, ttl 84) (label 825140, exp 0, ttl 0) (label 262165, exp 4, [S], ttl 42)
	0x0000:  0a01 0102 0a07 0302 0800 005d 0012 0001  ...........]....
	0x0010:  ba1d e962 0000 0000 953c 0000 0000 0000  ...b.....<......
	0x0020:  1011 1213 1415 1617 1819 1a1b 1c1d 1e1f  ................
	0x0030:  2021 2223 2425 2627 2829 2a2b 2c2d 2e2f  .!"#$%&'()*+,-./
	0x0040:  3031 3233 3435 3637                      01234567
00:00:0a:07:03:02 > 00:00:00:03:01:00, ethertype MPLS unicast (0x8847), length 102: MPLS (label 3, exp 0, ttl 254) (label 282624, exp 0, ttl 84) (label 840324, exp 0, ttl 0) (label 262165, exp 2, [S], ttl 117)
	0x0000:  0a01 0102 0a07 0302 0800 6a51 0012 0002  ..........jQ....
	0x0010:  bb1d e962 0000 0000 2a47 0000 0000 0000  ...b....*G......
	0x0020:  1011 1213 1415 1617 1819 1a1b 1c1d 1e1f  ................
	0x0030:  2021 2223 2425 2627 2829 2a2b 2c2d 2e2f  .!"#$%&'()*+,-./
	0x0040:  3031 3233 3435 3637                      01234567
```