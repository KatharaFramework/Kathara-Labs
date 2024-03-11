# 02-POX Core Object

## Introduction

You can put your Python code wherever you like, as long as POX can find it.
One of the top-level directories in POX is called `ext`. Indeed, POX automatically adds `ext` folder to the Python
search path.

The POX core object is a rendezvous between components:

* no need of import statements
* components register themselves on the core object
* other components will query the core object

It can be convenient for a component to "register" an API-providing object on the core object. You can use
core.register( ) or core.registerNew( ).

The following command is used to import the core object: ```from pox.core import core```.

## Lab

We have created two POX components:

* the component A implements: a string attribute named `hello_message`, a method to print the `hello_message` attribute
  on screen, and register itself in the POX Core.
* the component B implements a method that calls the `print` method of component A at startup.

![Network Scenario](../images/image1.png)

So, now we are using custom components and not a default one.

### Test the implementation

To run the network scenario, open a terminal in the scenario directory and type:
```bash
kathara lstart 
```

Launch in the root@controller:
```
python3.9 /pox/pox.py A B openflow.of_01 -port=6653
``` 

You will obtain:

```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al. 

# Result of component B
hello_message

# normal warning, don't worry
WARNING:version:Support for Python 3 is experimental.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switch
INFO:openflow.of_01:[e6-b1-b4-df-ec-42 1] connected
```

To undeploy the network scenario, open a terminal in the network scenario directory and type:
```bash
kathara lclean
```
