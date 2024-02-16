import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.recoco import Timer
from pox.lib.addresses import EthAddr
from pox.lib.packet.ethernet import ethernet
from pox.lib.packet.arp import arp
from pox.lib.addresses import IPAddr, EthAddr
from pox.lib.util import dpidToStr
from pox.lib.revent.revent import EventMixin
from pox.lib.revent.revent import Event
from datetime import datetime


log = core.getLogger()
MIN_SWITCH = 4


class Link:
    def __init__(self, sid1, sid2, dpid1, port1, dpid2, port2):
        self.name = str(sid1) + "_" + str(sid2)
        self.sid1 = sid1
        self.sid2 = sid2
        self.dpid1 = dpidToStr(dpid1)
        self.dpid2 = dpidToStr(dpid2)
        self.port1 = int(port1)
        self.port2 = int(port2)
        self.flow = 0



class linkDiscovery():

    def __init__(self):
        core.openflow.addListeners(self)

        # dictionary to store information about switches
        self.switches = {}

        # dictionary to store information about links between switches
        self.links = {}

        # dictionary to map switch identifiers to switch datapath IDs
        self.sw_id = {}

        # list for all rememeber all connections
        self.connections_list = []

        # fake mac address for link discovery
        self.fake_mac = EthAddr("00:11:22:33:44:55")

        # id to count connections_list
        self.id = 1

        # every 6 seconds sendProbes function is called
        Timer(6, self.sendProbes, recurring=True)


    def _handle_ConnectionUp(self, event):
        # Event handler method that is called when a new OpenFlow connection is established

        # Associates the current connection ID with the switch ID
        self.sw_id[self.id] = event.dpid

        # Stores information about switch
        self.switches[event.dpid] = event.ofp.ports

        # install a flow rule for network discovery
        self.install_flow_rule(event.dpid)

        # adds the new connection to the list of connections
        self.connections_list.append(event.connection)

        # print("Connection Up: " + dpidToStr(event.dpid) + ", " + str(self.id))

        # run the search of the host, I run it from the link discovery to allow order and not crash of my system. I use the following command to never have problem due to connection problem of the switches.
        if self.id >= MIN_SWITCH:
            core.hostDiscovery.search_host(self.connections_list)

        # increment connection ID
        self.id += 1


    def _handle_PacketIn(self, event):
        # Extracts the Ethernet frame from the event
        eth_frame = event.parsed

        # Checks if the source MAC address of the frame is equal to my fake gateway
        if eth_frame.src == self.fake_mac:

            # take information from frame
            eth_dst = eth_frame.dst.toStr().split(":")
            sid1 = int(eth_dst[4])
            dpid1 = self.sw_id[sid1]
            port1 = int(eth_dst[5])
            dpid2 = event.dpid
            sid2 = list(self.sw_id.keys())[list(self.sw_id.values()).index(dpid2)]
            port2 = event.ofp.in_port

            # Checks if the link between sid1 and sid2 is not already in the links dictionary

            if str(sid1) + "_" + str(sid2) not in self.links:

                # creates a new Link object and adds it to the dictionary
                link = Link(sid1, sid2, dpid1, port1, dpid2, port2)
                self.links[link.name] = link

                print("discovered new link: " + link.name)
                print(link.__dict__)

                graph = core.networkGraph.graph
                core.networkGraph.update_graph(graph,sid1,sid2,link.flow)


    def sendProbes(self):
        # iterates over the keys of the switches
        for sid in self.sw_id:

            # take dpid of the switch (for each key)
            dpid = self.sw_id[sid]

            # iterates over the ports of the selected switch
            for port in self.switches[dpid]:

                # condition excludes the special port used for flooding
                if port.port_no != 65534:

                    # fake source mac address (used in class)
                    mac_src = self.fake_mac

                    # fake destination mac address with sid of the wanted destination switch
                    mac_dst = EthAddr("00:00:00:00:" + str(sid) + ":" + str(port.port_no))

                    # creates ethernet frame, set ARP type, set source-destination-ARPpayload
                    ether = ethernet()
                    ether.type = ethernet.ARP_TYPE
                    ether.src = mac_src
                    ether.dst = mac_dst
                    ether.payload = arp()

                    # creates OpenFlow packet, put frame inside, send of message to selected switch
                    msg = of.ofp_packet_out()
                    msg.data = ether.pack()
                    msg.actions.append(of.ofp_action_output(port=port.port_no))
                    core.openflow.sendToDPID(dpid, msg)


    def install_flow_rule(self, dpid):
        # Creates an OpenFlow flow modification message
        msg = of.ofp_flow_mod()

        # set high priority
        msg.priority = 50000

        # set match structure specifying that the source MAC address should be 00:11:22:33:44:55
        match = of.ofp_match(dl_src=self.fake_mac)

        # set match to flow modification message, send message
        msg.match = match

        # set action (sends the packet to the controller), send message
        msg.actions = [of.ofp_action_output(port=of.OFPP_CONTROLLER)]
        core.openflow.sendToDPID(dpid, msg)



def launch():
    core.registerNew(linkDiscovery)
