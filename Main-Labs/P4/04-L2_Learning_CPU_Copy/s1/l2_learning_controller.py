import shlex
import subprocess

from scapy.all import sniff, Packet, BitField
from scapy.layers.l2 import Ether


class CpuHeader(Packet):
    name = 'CpuPacket'
    fields_desc = [BitField('macAddr', 0, 48), BitField('ingress_port', 0, 16)]


class L2Controller(object):
    def learn(self, learning_data):
        for mac_addr, ingress_port in learning_data:
            print("mac: %012X ingress_port: %s " % (mac_addr, ingress_port))

            proc = subprocess.Popen(
                shlex.split('bash -c \'simple_switch_CLI <<< "table_add smac NoAction 0x%012X => "\'' % mac_addr),
                stdout=subprocess.DEVNULL
            )
            proc.wait()
            proc.terminate()

            proc = subprocess.Popen(
                shlex.split(
                    'bash -c \'simple_switch_CLI <<< "table_add dmac_forward forward_to_port 0x%012X => %s"\'' % (
                        mac_addr, ingress_port)),
                stdout=subprocess.DEVNULL
            )
            proc.wait()
            proc.terminate()

    def recv_msg_cpu(self, packet):
        if packet.type == 0x1234:
            cpu_header = CpuHeader(bytes(packet.payload))
            self.learn([(cpu_header.macAddr, cpu_header.ingress_port)])

    def run_cpu_port_loop(self):
        sniff(iface="cpu", prn=self.recv_msg_cpu)


if __name__ == "__main__":
    L2Controller().run_cpu_port_loop()
