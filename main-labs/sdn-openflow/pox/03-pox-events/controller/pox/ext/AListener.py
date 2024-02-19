from pox.core import core
from pox.lib.revent.revent import Event
from pox.lib.revent.revent import EventMixin


class pktInSeen(Event):
    def __init__(self):
        Event.__init__(self)


class AListener(EventMixin):
    _eventMixin_events = {pktInSeen}

    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_PacketIn(self, event):
        print("*** From AListener: packetIn captured!")
        self.raiseEvent(pktInSeen)


def launch():
    component = AListener()
    core.register("A", component)
