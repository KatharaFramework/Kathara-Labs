import pox.openflow.libopenflow_01 as of
from pox.core import core
from pox.lib.packet.ethernet import ethernet
from pox.lib.util import dpidToStr
from datetime import datetime
from pox.lib.recoco import Timer
import networkx as nx

log = core.getLogger()

class maxThroughputRouting:

    def __init__(self):

        # Listener for OpenFlow
        core.openflow.addListeners(self)

        # Dictionary to store flows
        self.dict_flows = {}

        # Timer to see flows situation in the network
        Timer(30, self.ask_FlowStats, recurring=True)


    def _handle_PacketIn(self, event):
        # event handler that extracts the parsed packet from it (the event)
        packet = event.parsed
        
        # Checks if the packet is an IPv4 packet
        # Checks source and destination MAC addresses are not equal to the gateway's MAC address of Component_ARP (the fake one)
        if (packet.find('ipv4') and packet.src != core.Component_ARP.gateway_MAC and packet.dst != core.Component_ARP.gateway_MAC):

            # extracts the source and destination IP addresses from the IPv4 payload
            ip_packet = packet.payload
            source_ip = ip_packet.srcip
            destination_ip = ip_packet.dstip

            # call routing method
            self.routing_flows(source_ip,destination_ip)
            
            # creates a new ofp_packet_out message
            msg = of.ofp_packet_out()

            # sets data with the received packet
            msg.data = packet

            # adds an output action to send the packet to the table
            msg.actions.append(of.ofp_action_output(port=of.OFPP_TABLE))

            # sends the message to the switch
            event.connection.send(msg)

     
    def routing_flows(self,src_host_ip,dst_host_ip):

        # get graph object with class networkGraph
        graph = core.networkGraph.graph

        # get the switch DPID of the src and of the dst, the port on the switch to which the destination host is connected
        sw_src = core.hostDiscovery.hosts[src_host_ip]["switch"]
        sw_dst = core.hostDiscovery.hosts[dst_host_ip]["switch"]
        sw_to_host_port = core.hostDiscovery.hosts[dst_host_ip]["port"]

        # get the id of the source switch and of the destination switch
        dict_switch_id=core.linkDiscovery.sw_id
        for key, value in dict_switch_id.items():
            if value == sw_src:
                source_id = key
            if value == sw_dst:
                dest_id = key

        # calculates shortest path between source and destination switches based on edge weights
        path = list(nx.shortest_path(graph, source_id, dest_id, weight="weight"))

        # get path links as a list of tuple
        path_links = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        # -> [(1,3),(3,4)] for example
        
        log.info(f"found path from {src_host_ip} to {dst_host_ip} -> {path_links}")

        # flow identified by src ip, dst ip, Ethernet type (we look at IPV4)
        flow_id = (src_host_ip, dst_host_ip, ethernet.IP_TYPE)
        
        # update the dict_flows with the new paths
        self.dict_flows[flow_id] = path_links

        # initializes an OpenFlow flow modification message
        msg = of.ofp_flow_mod()

        # sets timeout to remove the flow
        msg.idle_timeout = 25
        
        # flow removed message will be sent when the rule expires
        msg.flags = of.OFPFF_SEND_FLOW_REM

        # condition for the flow rule
        msg.match = of.ofp_match(dl_type=ethernet.IP_TYPE, nw_src=src_host_ip, nw_dst=dst_host_ip)


        # only a switch between the hosts, like .11 and .12
        if len(path) == 1:

            # set output action of the message to the port connected to the destination host
            msg.actions = [of.ofp_action_output(port=sw_to_host_port)]  

            # send the message to the destination switch
            core.openflow.sendToDPID(sw_dst, msg)

        # more switches between the hosts
        else:

            # iterate over each link in the path
            for sw in path_links:

                source_dpid = core.linkDiscovery.sw_id[sw[0]]
                link_id = f"{sw[0]}_{sw[1]}"
                output_port = core.linkDiscovery.links[link_id].port1

                # increment flow on the edge by 1
                core.networkGraph.add_weight(graph,sw[0],sw[1],1)

                # take flows of that link to print it
                flow_weight = graph[sw[0]][sw[1]]["weight"]

                # set the output action of the message to the current output port
                msg.actions = [of.ofp_action_output(port=output_port)]

                # send the message to the source switch
                core.openflow.sendToDPID(source_dpid, msg)

                print(f"  ->  link {link_id} has {flow_weight} flows")

                # path is ended, this switch is the destination switch
                if sw[1] == dest_id:
                    # set action of the message to the port connected to the destination host
                    msg.actions = [of.ofp_action_output(port=sw_to_host_port)]

                    # send the message to the destination switch
                    core.openflow.sendToDPID(sw_dst, msg)



    def _handle_FlowRemoved(self, event):
        # Checks if the flow removal is due to an idle timeout (it has been idle for too long)
        if event.idleTimeout:
            flow_match = event.ofp.match

            dict_switch_id=core.linkDiscovery.sw_id
            sw_id = [key for key, value in dict_switch_id.items() if value == event.dpid]

            # tell that the flow has been removed
            log.info(f"  ->  switch {sw_id,dpidToStr(event.dpid)} removed flow from {flow_match.nw_src} to {flow_match.nw_dst}")

            # now it is needed to remove the flow from the network_occupation (total weight)
            flow_id = (flow_match.nw_src, flow_match.nw_dst, flow_match.dl_type)

            if flow_id in self.dict_flows.keys():

                # get graph object with class networkGraph
                graph = core.networkGraph.graph

                # If the flow is present in the dictionary, it decreases the flow counter for every link used by the flow
                for link in self.dict_flows[flow_id]:
                    core.networkGraph.remove_weight(graph,link[0],link[1],1)

                # removes the flow from the dict_flows dictionary
                self.dict_flows.pop(flow_id)



    def _handle_FlowStatsReceived (self, event):

        # triggered when the controller receives statistics about flows from the switches
        total_bytes = 0
        total_flows = 0

        # iterates over the flow statistics received in the event
        for f in event.stats:
            # checks if it is IP_TYPE, indicating an IPv4 flow
            if ethernet.IP_TYPE == f.match.dl_type:
                total_bytes += f.byte_count
                total_flows += 1

        dict_switch_id=core.linkDiscovery.sw_id
        sw_id = [key for key, value in dict_switch_id.items() if value == event.dpid]

        print(f"switch {sw_id} has {total_bytes} bytes and {total_flows} flows")


    def ask_FlowStats(self):

        #  For each connection, it sends an OpenFlow statistics request message (flow statistics)
        for connection in core.openflow.connections:

            # This triggers the switch to respond with flow statistics.
            connection.send(of.ofp_stats_request(body=of.ofp_flow_stats_request()))


def launch():
    core.registerNew(maxThroughputRouting)
