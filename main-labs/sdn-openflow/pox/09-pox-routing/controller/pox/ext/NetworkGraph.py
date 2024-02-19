import networkx as nx
from pox.core import core

log = core.getLogger()


class NetworkGraph:

    def __init__(self):
        core.openflow.addListeners(self)

        # New undirected graph is created using networkx library
        self.graph = nx.Graph()

    def update_graph(self, graph_element, sid1, sid2, weight):

        # add node (switch) with sid1
        if not graph_element.has_node(sid1):
            graph_element.add_node(sid1)

        # add node (switch) with sid2
        if not graph_element.has_node(sid2):
            graph_element.add_node(sid2)

        # add edge (link between switches) between sid1 and sid2
        if not graph_element.has_edge(sid1, sid2):
            graph_element.add_edge(sid1, sid2, weight=weight)

        print("graph updated")

    def add_weight(self, graph_element, node_a, node_b, add_link_weight):
        # If the edge exists, add the weight. It is called by the max_throughput_routing Function
        if graph_element.has_edge(node_a, node_b):
            graph_element[node_a][node_b]["weight"] += add_link_weight
        else:
            log.error(f"node not found in the graph")

    def remove_weight(self, graph_element, node_a, node_b, remove_link_weight):
        # If the edge exists, remove the weight. It is called by the max_throughput_routing Function
        if graph_element.has_edge(node_a, node_b):
            graph_element[node_a][node_b]["weight"] -= remove_link_weight
        else:
            log.error(f"node not found in the graph")


def launch():
    core.registerNew(NetworkGraph)
