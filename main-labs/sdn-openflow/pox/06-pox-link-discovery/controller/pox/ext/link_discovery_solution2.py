import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.addresses import EthAddr
from pox.lib.packet.arp import arp
from pox.lib.packet.ethernet import ethernet
from pox.lib.recoco import Timer
from pox.lib.util import dpidToStr


class Link:

    def __init__(self, sid1, sid2, dpid1, port1, dpid2, port2):
        self.name = str(sid1) + "_" + str(sid2)
        self.sid1 = sid1
        self.sid2 = sid2
        self.dpid1 = dpidToStr(dpid1)
        self.dpid2 = dpidToStr(dpid2)
        self.port1 = int(port1)
        self.port2 = int(port2)


class LinkDiscovery:

    def __init__(self):
        self.switches = {}  # <key: dpid; value: list of switch's ports>
        self.links = {}  # list of link objects
        self.switch_id = {}  # <key: a progressive ID; value: the dpid of the switch>
        self.id = 1  # use this to assign progressive IDs to connecting switches
        core.openflow.addListeners(self)  # add the current object to the openflow listeners
        Timer(5, self.sendProbes, recurring=True)  # every 5 seconds executes the sendProbe method

    def _handle_ConnectionUp(self, event):

        print("Connection Up: " + dpidToStr(event.dpid))

        # update the defined dictionaries
        self.switches[event.dpid] = event.ofp.ports
        self.switch_id[self.id] = event.dpid

        # run the install_flow_rule method
        self.install_flow_rule(event.dpid)
        self.id += 1

    def _handle_PacketIn(self, event):
        eth_frame = event.parsed  # extract the ethernet frame from the incoming packet in
        if eth_frame.src == EthAddr("00:11:22:33:44:55"):  # is this a discovery message?

            # parse the packet to extract the relevant information
            # sid1 and sid2 should contain the switch ID of the switches connected by the discovered link
            # dpid1 and dpid2 should contain the dpid of the switches connected by the discovered link
            save = str(eth_frame.dst).split(":")
            sid1 = int(save[4])
            port1 = int(save[5])
            dpid1 = self.switch_id[sid1]

            dpid2 = event.dpid
            port2 = event.ofp.in_port
            sid2 = int(list(self.switch_id.keys())[list(self.switch_id.values()).index(dpid2)])

            link = Link(sid1, sid2, dpid1, port1, dpid2, port2)
            if link.name not in self.links:
                self.links[link.name] = link
                print("discovered new link: " + link.name)
                print(link.__dict__)

    def sendProbes(self):
        for sid in self.switch_id:
            dpid = self.switch_id[sid]
            for port in self.switches[dpid]:  # iterate over all the ports of the current switch
                if port.port_no != of.OFPP_CONTROLLER:  # if the current port is not the one connecting to the controller
                    mac_src = EthAddr(
                        "00:11:22:33:44:55")  # set the mac address so that it allows to distinguish that the frame carries a discovery message
                    mac_dst = EthAddr("00:00:00:00:" + str(sid) + ":" + str(
                        port.port_no))  # encode in the mac_dst the relevant information
                    ether = ethernet()  # create the message to inject in the data plane
                    ether.type = ethernet.ARP_TYPE
                    ether.src = mac_src
                    ether.dst = mac_dst
                    ether.payload = arp()
                    msg = of.ofp_packet_out()
                    msg.data = ether.pack()
                    msg.actions.append(of.ofp_action_output(
                        port=port.port_no))  # instruct the switch to send the packet out of the current inspected port
                    core.openflow.sendToDPID(dpid, msg)  # send the packet_out message to the switch

    @staticmethod
    def install_flow_rule(dpid):
        # Install in a proactive way
        msg = of.ofp_flow_mod()  # Create an empty flow_mod message
        msg.priority = 50000
        match = of.ofp_match(dl_src=EthAddr("00:11:22:33:44:55"))  # The match is an object
        msg.match = match
        msg.actions = [of.ofp_action_output(port=of.OFPP_CONTROLLER)]
        core.openflow.sendToDPID(dpid, msg)


def launch():
    LinkDiscovery()
