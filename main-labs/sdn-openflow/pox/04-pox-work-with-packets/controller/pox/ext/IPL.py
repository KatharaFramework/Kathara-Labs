from pox.core import core
from pox.lib.revent.revent import Event


class pktInSeen(Event):
    def __init__(self):
        Event.__init__(self)


class IPL:

    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        ip = packet.find('ipv4')
        if ip is None:
            print('NOT IP')
        else:
            print('* * * Found IP packet!')


def launch():
    component = IPL()
    core.register("IPL", component)
