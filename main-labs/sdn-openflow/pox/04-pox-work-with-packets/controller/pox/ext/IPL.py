from pox.core import core
from pox.lib.revent.revent import EventMixin
from pox.lib.revent.revent import Event
import pox.lib.packet as pkt

class pktInSeen (Event):
	def __init__ (self):
		Event.__init__(self)

class Component_IPL ():	
	
	def __init__ (self):
		core.openflow.addListeners(self)
		
	def _handle_PacketIn (self, event):
		packet = event.parsed
		ip = packet.find('ipv4')
		if ip is None:
			print('NOT IP')
		else:
			print('* * * Found IP packet!')
		
	
def launch ( ):
	component = Component_IPL()
	core.register("IPL", component)
