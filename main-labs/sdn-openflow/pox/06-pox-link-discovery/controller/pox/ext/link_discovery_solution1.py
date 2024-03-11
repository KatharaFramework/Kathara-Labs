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
        self.switches = {}
        self.links = {}
        self.switch_id = {}
        self.id = 1
        core.openflow.addListeners(self)
        Timer(5, self.sendProbes, recurring=True)

    def _handle_ConnectionUp(self, event):
        self.switch_id[self.id] = event.dpid
        self.switches[event.dpid] = event.ofp.ports
        self.install_flow_rule(event.dpid)
        print("Connection Up: " + dpidToStr(event.dpid) + ", " + str(self.id))
        self.id += 1

    def _handle_PacketIn(self, event):
        eth_frame = event.parsed
        if eth_frame.src == EthAddr("00:11:22:33:44:55"):
            eth_dst = eth_frame.dst.toStr().split(':')
            sid1 = int(eth_dst[4])
            dpid1 = self.switch_id[sid1]
            port1 = int(eth_dst[5])
            dpid2 = event.dpid
            sid2 = list(self.switch_id.keys())[list(self.switch_id.values()).index(dpid2)]
            port2 = event.ofp.in_port
            link = Link(sid1, sid2, dpid1, port1, dpid2, port2)
            if link.name not in self.links:
                self.links[link.name] = link
                print("discovered new link: " + link.name)
                print(link.__dict__)

    def sendProbes(self):
        for sid in self.switch_id:
            dpid = self.switch_id[sid]
            for port in self.switches[dpid]:
                if port.port_no != 65534:
                    mac_src = EthAddr("00:11:22:33:44:55")
                    mac_dst = EthAddr("00:00:00:00:" + str(sid) + ":" + str(port.port_no))
                    ether = ethernet()
                    ether.type = ethernet.ARP_TYPE
                    ether.src = mac_src
                    ether.dst = mac_dst
                    ether.payload = arp()
                    msg = of.ofp_packet_out()
                    msg.data = ether.pack()
                    msg.actions.append(of.ofp_action_output(port=port.port_no))
                    core.openflow.sendToDPID(dpid, msg)

    @staticmethod
    def install_flow_rule(dpid):
        msg = of.ofp_flow_mod()
        msg.priority = 50000
        match = of.ofp_match(dl_src=EthAddr("00:11:22:33:44:55"))
        msg.match = match
        msg.actions = [of.ofp_action_output(port=of.OFPP_CONTROLLER)]
        core.openflow.sendToDPID(dpid, msg)


def launch():
    LinkDiscovery()
