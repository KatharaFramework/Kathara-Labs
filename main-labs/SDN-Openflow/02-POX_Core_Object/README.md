# 02-POX_Core_Object

## Introduction

You can put your Python code wherever you like, as long as POX can find it. One of the top-level directories in POX is called "ext". Indeed, POX automatically adds “ext” folder to the Python search path.

Each component must define a launch function: it is a function that POX calls to tell the component to initialize itself and it specifies how command line arguments are passed to the component.

The POX core object is a rendezvous between components:
* no need of import statements
* components register themselves on the core object
* other components will query the core object

The following command is used to import the core object: ```from pox.core import core```.

It can be convenient for a component to "register" an API-providing object on the core object. There are two ways to register a component: 
* core.register( )
* core.registerNew( )


## Lab

We have created two POX components:
* the component A implements: a string attribute named "hello_message", a method to print the "hello_message" attribute on screen, and register itself in the POX Core.
* the component B implements a method that calls the “print” method of component A at startup.

So, now we are using custom components and not a default one.

### Test the implementation

Launch ```kathara lstart``` in the main terminal, wait until the lab is created

Launch ```kathara connect controller``` in the main terminal

Launch ```./home/pox/pox.py A B openflow.of_01 -port=6653``` in the root@controller

You will obtain: 
```
# general informations
POX 0.7.0 (gar) / Copyright 2011-2020 James McCauley, et al. 

# Result of component B
Testo prova

# normal warning, not be worry
WARNING:version:POX requires one of the following versions of Python: 3.6 3.7 3.8 3.9
WARNING:version:You're running Python 3.11.
WARNING:version:If you run into problems, try using a supported version.
INFO:core:POX 0.7.0 (gar) is up.

# connection of the switch
INFO:openflow.of_01:[e6-b1-b4-df-ec-42 1] connected
```

Close the root@controller with ```exit```

Close the lab with ```kathara lclean```

