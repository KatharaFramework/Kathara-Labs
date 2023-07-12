import shlex
import struct
import subprocess

import nnpy

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

    def unpack_digest(self, msg, num_samples):
        digest = []
        print(len(msg), num_samples)
        starting_index = 32
        for sample in range(num_samples):
            mac0, mac1, ingress_port = struct.unpack(">LHH", msg[starting_index:starting_index + 8])
            starting_index += 8
            mac_addr = (mac0 << 16) + mac1
            digest.append((mac_addr, ingress_port))

        return digest

    def recv_msg_digest(self, msg):
        topic, device_id, ctx_id, list_id, buffer_id, num = struct.unpack("<iQiiQi", msg[:32])
        digest = self.unpack_digest(msg, num)
        self.learn(digest)

        # Should ack buffer but we don't :)

    def run_digest_loop(self):
        sub = nnpy.Socket(nnpy.AF_SP, nnpy.SUB)
        notifications_socket = "ipc:///tmp/bmv2-0-notifications.ipc"
        sub.connect(notifications_socket)
        sub.setsockopt(nnpy.SUB, nnpy.SUB_SUBSCRIBE, '')

        while True:
            msg = sub.recv()
            self.recv_msg_digest(msg)

if __name__ == "__main__":
    L2Controller().run_digest_loop()
