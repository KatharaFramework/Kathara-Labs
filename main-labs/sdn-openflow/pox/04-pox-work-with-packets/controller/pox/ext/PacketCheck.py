from pox.core import core
from pox.lib.packet import ethernet as pkt


class PacketCheck:

    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        if packet.type == pkt.IP_TYPE:
            print("*** From Component: IP packet detected!")
        else:
            print("*** From Component: packet detected NOT IP!")


def launch():
    PacketCheck()
