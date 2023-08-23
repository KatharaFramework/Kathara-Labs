# Getting-Started

This tutorial provides the bases for using the Kathará Python API.

## Installation 
Installing the Kathará Python API is super easy since you can find the latest stable version on [PyPI](https://pypi.org/project/kathara/). 

```bash
python3 -m pip install "kathara[pyuv]"
```

⚠️ **WARNING:** `[pyuv]` is required to install `pyuv` as an extra dependency, since it may be blocked by PyPI from being downloaded from a git repository, giving this error:
```
Packages installed from PyPI cannot depend on packages which are not also hosted on PyPI.
```

If you are getting this error, first install Kathará without `[pyuv]` and then re-execute the command with the extra dependency:
```bash
python3 -m pip install kathara
python3 -m pip install "kathara[pyuv]"
```

If the problem persists, install `pyuv` manually and then install Kathará:
```bash
python3 -m pip install git+https://github.com/saghul/pyuv@master#egg=pyuv
python3 -m pip install kathara
```

## Getting Started

To interact with Kathará, you first need to create a network scenario.

```python
from Kathara.model.Lab import Lab
from Kathara.manager.Kathara import Kathara

lab = Lab("kathara-tutorial")
```

You can now create devices. 

```python
pc1 = lab.new_machine("pc1")
pc2 = lab.new_machine("pc2")
```

And you can connect them. 

```python
lab.connect_machine_to_link(pc1.name, "A")
lab.connect_machine_to_link(pc2.name, "A")
```

Now you are ready to deploy the network scenario. 

```python
Kathara.get_instance().deploy_lab(lab)
```

You can check that the devices are up and running. 

```python
print(next(Kathara.get_instance().get_machines_stats(lab_name=lab.name)))
```

This is an example of output. 

```bash
{'kathara_user-cfp7yzdwcy6z7geo1lgx7g_pc1_j7CX6Y6grTLV4tO63dCvXw': {'network_scenario_id': 'j7CX6Y6grTLV4tO63dCvXw', 'name': 'pc1', 'container_name': 'kathara_user-cfp7yzdwcy6z7geo1lgx7g_pc1_j7CX6Y6grTLV4tO63dCvXw', 'user': 'user-cfp7yzdwcy6z7geo1lgx7g', 'status': 'running', 'image': 'kathara/quagga:latest', 'pids': 1, 'cpu_usage': '0.00%', 'mem_usage': '916.0 KB / 15.37 GB', 'mem_percent': '0.01 %', 'net_usage': '572.0 B / 0 B'}, 'kathara_user-cfp7yzdwcy6z7geo1lgx7g_pc2_j7CX6Y6grTLV4tO63dCvXw': {'network_scenario_id': 'j7CX6Y6grTLV4tO63dCvXw', 'name': 'pc2', 'container_name': 'kathara_user-cfp7yzdwcy6z7geo1lgx7g_pc2_j7CX6Y6grTLV4tO63dCvXw', 'user': 'user-cfp7yzdwcy6z7geo1lgx7g', 'status': 'running', 'image': 'kathara/quagga:latest', 'pids': 1, 'cpu_usage': '0.00%', 'mem_usage': '916.0 KB / 15.37 GB', 'mem_percent': '0.01 %', 'net_usage': '2.55 KB / 0 B'}}
```

This is just an example of what you can do with Kathará Python API.

## What's next?
The API also allows you to manage network scenarios and devices filesystem to create more complex scenarios. 
If you are interested follow the [Managing Filesystem](../managing-filesystem) tutorial. 

## Documentation 
You can find a complete overview of the Kathará API at [docs](https://github.com/KatharaFramework/Kathara/wiki/Kathara-API-Docs).  