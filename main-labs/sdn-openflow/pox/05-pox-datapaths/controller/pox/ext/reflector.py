from pox.core import core
from pox.lib.revent.revent import Event
from pox.lib.packet import ethernet as pkt
import pox.openflow.libopenflow_01 as of

class reflector ():
	
	def __init__ (self):
		core.openflow.addListeners(self)
		
	def _handle_PacketIn (self, event):
		packet = event.parsed
		source = packet.src
		destination = packet.dst
		
		eth_frame = packet
		
		eth_frame.src = destination
		eth_frame.dst = source
		
		msg = of.ofp_packet_out()
		msg.data = eth_frame.raw	#or use event.data
		action = of.ofp_action_output(port = event.port)
		
		msg.actions.append(action)
		
		connection = event.connection
		connection.send(msg)

		#print(packet)
		#print(eth_frame)
		print("Received from (and sent back to): "+str(source))
		print("The destination before was: "+str(destination))
		print("Port used: "+str(event.port))
	
def launch ( ):
	component = reflector()
