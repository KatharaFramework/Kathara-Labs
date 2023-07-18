import logging
import os.path

from Kathara.manager.Kathara import Kathara
from Kathara.model.Lab import Lab

logger = logging.getLogger("Kathara")
logger.setLevel(logging.INFO)

logger.info("Creating Lab BGP Announcement...")
lab = Lab("BGP Announcement")

logger.info("Creating router1...")
# Create router1 with image "kathara/frr"
router1 = lab.new_machine("router1", **{"image": "kathara/frr"})

# Create and connect router1 interfaces
lab.connect_machine_to_link(router1.name, "A")
lab.connect_machine_to_link(router1.name, "B")


logger.info("Creating router2...")
# Create router2 with image "kathara/frr"
router2 = lab.new_machine("router2", **{"image": "kathara/frr"})

# Create and connect router1 interfaces
lab.connect_machine_to_link(router2.name, "A")
lab.connect_machine_to_link(router2.name, "C")

logger.info("Configuring router1...")

# Configure router1 startup commands
lab.create_file_from_list(
    [
        "/sbin/ifconfig eth0 193.10.11.1 up",
        "/sbin/ifconfig eth1 195.11.14.1 up",
        "/etc/init.d/frr start"
    ],
    "router1.startup"
)

# Configuring BGP on router1
router1.create_file_from_path(os.path.join("assets", "router1-frr.conf"), "/etc/frr/frr.conf")
router1.create_file_from_path(os.path.join("assets", "daemons"), "/etc/frr/daemons")
router1.create_file_from_string(content="service integrated-vtysh-config\n", dst_path="/etc/frr/vtysh.conf")
router1.update_file_from_string(content="hostname router1-frr\n", dst_path="/etc/frr/vtysh.conf")

logger.info("Configuring router2...")

# Configure router2 startup commands
lab.create_file_from_list(
    [
        "/sbin/ifconfig eth0 193.10.11.2 up",
        "/sbin/ifconfig eth1 200.1.1.1 up",
        "/etc/init.d/frr start"
    ],
    "router2.startup"
)
# Configuring BGP on router2
router2.create_file_from_path(os.path.join("assets", "router2-frr.conf"), "/etc/frr/frr.conf")
router2.create_file_from_path(os.path.join("assets", "daemons"), "/etc/frr/daemons")
router2.create_file_from_string(content="service integrated-vtysh-config\n", dst_path="/etc/frr/vtysh.conf")
router2.update_file_from_string(content="hostname router2-frr\n", dst_path="/etc/frr/vtysh.conf")

logger.info("Deploying BGP Announcement lab...")
Kathara.get_instance().deploy_lab(lab)

logger.info("Connecting to router1...")
logger.info("Try inspecting the routing tables: 'ip route'")
logger.info("Or log into the control plane: 'vtysh'")
Kathara.get_instance().connect_tty(router1.name, lab_name=lab.name)

logger.info("Connecting to router2...")
logger.info("Try inspecting the routing tables: 'ip route'")
logger.info("Or log into the control plane: 'vtysh'")
Kathara.get_instance().connect_tty(router2.name, lab_name=lab.name)

logger.info("Undeploying BGP Announcement lab...")
Kathara.get_instance().undeploy_lab(lab_name=lab.name)
