# P4 BMv2 Examples

Kathar&aacute; examples of P4 labs, taken from [nsg-ethz/p4-learning](https://github.com/nsg-ethz/p4-learning).

## Prerequisites

Some of the labs use Scapy to craft arbitrary packets. Hence, you need to build the `kathara/scapy` image.

From this folder, open a terminal and type:
```
docker build -t kathara/scapy .
```

## Notes

Some implementation details, like MAC address assignment and IP assignment, could differ from the original solutions.
As an example, the MAC address `ff:ff:ff:ff:ff:ff` cannot be used in Kathar&aacute;.