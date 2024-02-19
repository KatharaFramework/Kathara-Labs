import ipaddress

import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.addresses import EthAddr
from pox.lib.addresses import IPAddr
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet

log = core.getLogger()


class ARP:
    def __init__(self) -> None:
        core.openflow.addListeners(self)
        self.network_mask = "255.255.255.0"
        self.gateway_IP = IPAddr("10.0.0.1")
        self.gateway_MAC = EthAddr("11:11:11:11:11:11")

    def _handle_PacketIn(self, event):
        # This method handles ARP requests. By checking if they are directed to the gateway or hosts in the network, it installs flow rules and handles ARP replies.

        packet = event.parsed

        # checks if the packet type is ARP and if the ARP packet is an ARP request (not done for host discovery)
        if packet.type == packet.ARP_TYPE and packet.payload.opcode == arp.REQUEST:

            if packet.src != core.hostDiscovery.fake_mac_gw:

                # extracts the ARP payload from the packet
                packet_ARP = packet.payload

                log.info(f"ARP, Request who-has {packet_ARP.protodst} tell {packet_ARP.protosrc}")

                # creates an IPv4 network object using the destination IP address and the network mask
                ip_network = ipaddress.IPv4Network(f"{str(packet.payload.protodst)}/{self.network_mask}", strict=False)

                # checks if the gateway is not in the same network as the destination IP address
                # or if the destination IP address is the same as the gateway IP
                # This is True for ARP request for the gateway
                if ((ipaddress.IPv4Address(
                        str(self.gateway_IP)) not in ip_network) or packet.payload.protodst == self.gateway_IP):
                    self.handle_ARP_Request(event, packet_ARP, rule=True)

                # checks if the destination IP address is in the keys of the core.hostDiscovery.hosts
                # This is True for ARP requests for hosts in the network
                elif (packet.payload.protodst in core.hostDiscovery.hosts.keys()):
                    self.handle_ARP_Request(event, packet_ARP, rule=False)

            else:
                log.info(f"fake ARP REQUEST for host discovery")

    def handle_ARP_Request(self, event, packet_ARP, rule):
        # This method generates an ARP reply message, encapsulates it in an Ethernet frame, and sends it out as a packet-out message to the switch

        # Creates ARP reply message and set the opcode to indicate that it's an ARP reply
        arp_reply = arp()
        arp_reply.opcode = arp.REPLY

        # sets the source MAC address (hwsrc) of the ARP reply
        if rule:
            # This is True for ARP request for the gateway
            arp_reply.hwsrc = self.gateway_MAC
        else:
            # This is True for ARP requests for hosts in the network
            arp_reply.hwsrc = core.hostDiscovery.hosts[packet_ARP.protodst]["mac"]

        # set the destination MAC address (hwdst) of the ARP reply to the source MAC address (hwsrc) of the received ARP request
        arp_reply.hwdst = packet_ARP.hwsrc

        # swaps the source and destination IP addresses to complete the reply
        arp_reply.protosrc = packet_ARP.protodst
        arp_reply.protodst = packet_ARP.protosrc

        # Create ethernet frame
        ether = ethernet()

        # set its type to ARP
        ether.type = ethernet.ARP_TYPE

        # sets the destination MAC address (dst) of the Ethernet frame to the source MAC address of the received ARP request.
        ether.dst = packet_ARP.hwsrc

        # sets the source MAC address (src) of the Ethernet frame
        if rule:
            # This is True for ARP request for the gateway
            ether.src = self.gateway_MAC
        else:
            # This is True for ARP requests for hosts in the network
            ether.src = core.hostDiscovery.hosts[packet_ARP.protodst]["mac"]

        # sets the payload of the Ethernet frame to the ARP reply message
        ether.payload = arp_reply

        log.info(f"ARP, Reply {arp_reply.protosrc} is-at {arp_reply.hwsrc}")

        # create an OpenFlow packet-out message and send it
        msg = of.ofp_packet_out()
        msg.data = ether.pack()
        msg.actions.append(of.ofp_action_output(port=event.port))
        event.connection.send(msg)


def launch():
    core.registerNew(ARP)
