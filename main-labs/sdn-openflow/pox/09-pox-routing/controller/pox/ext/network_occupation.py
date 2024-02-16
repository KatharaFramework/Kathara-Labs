import networkx as nx
from datetime import datetime
from pox.core import core

log = core.getLogger()


class networkGraph:


    def __init__(self):
        core.openflow.addListeners(self)

        # New undirected graph is created using networkx library
        self.graph = nx.Graph()


    def update_graph(self,graph_element,sid1,sid2,weight):

        # add node (switch) with sid1
        if not graph_element.has_node(sid1):
            graph_element.add_node(sid1)

        # add node (switch) with sid2
        if not graph_element.has_node(sid2):
            graph_element.add_node(sid2)

        # add edge (link between switches) between sid1 and sid2
        if not graph_element.has_edge(sid1,sid2):
            graph_element.add_edge(sid1,sid2,weight=weight)

        print("graph updated")


    def add_weight(self, graph_element, nodeA, nodeB, add_link_weight):
        # If the edge exists, add the weight. It is called by the max_throughput_routing Function
        if graph_element.has_edge(nodeA,nodeB):
            graph_element[nodeA][nodeB]["weight"] += add_link_weight
        else:
            log.error(f"node not found in the graph")


    def remove_weight(self, graph_element, nodeA, nodeB, remove_link_weight):
        # If the edge exists, remove the weight. It is called by the max_throughput_routing Function
        if graph_element.has_edge(nodeA,nodeB):
            graph_element[nodeA][nodeB]["weight"] -= remove_link_weight
        else:
            log.error(f"node not found in the graph")


def launch():
    core.registerNew(networkGraph)
