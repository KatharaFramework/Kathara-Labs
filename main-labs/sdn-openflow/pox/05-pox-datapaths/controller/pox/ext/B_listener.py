from pox.core import core
from pox.lib.revent.revent import Event

class Component_B ():
	def __init__ (self, A):
		A.addListeners(self)
            
	def _handle_pktInSeen (self, event):
		print("*** From Component_B: A has seen an OFP packetIn!")
	
def launch ():
	listen_B = Component_B(core.A)
