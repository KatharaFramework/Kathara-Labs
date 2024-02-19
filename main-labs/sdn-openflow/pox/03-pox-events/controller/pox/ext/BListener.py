from pox.core import core


class BListener:
    def __init__(self, component):
        component.addListeners(self)

    def _handle_pktInSeen(self, event):
        print("*** From BListener: A has seen an OFP packetIn!")


def launch():
    BListener(core.A)
