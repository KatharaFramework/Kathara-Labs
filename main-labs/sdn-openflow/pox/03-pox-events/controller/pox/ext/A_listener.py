from pox.core import core
from pox.lib.revent.revent import EventMixin
from pox.lib.revent.revent import Event

class pktInSeen (Event):
	def __init__ (self):
		Event.__init__(self)

class Component_A (EventMixin):	
	_eventMixin_events = set([pktInSeen,])
	
	def __init__ (self):
		core.openflow.addListeners(self)
		
	def _handle_PacketIn (self, event):
		print("*** From Component_A: packetIn captured!")
		self.raiseEvent(pktInSeen)
	
def launch ( ):
	component = Component_A()
	core.register("A", component)
