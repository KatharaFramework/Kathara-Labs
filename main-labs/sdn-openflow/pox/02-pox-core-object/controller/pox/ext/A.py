from pox.core import core

class A():
	def __init__(self, arg):
		self.hello_message = arg
		
	def method_print(self):
		print(self.hello_message)
		
def launch():
	component = A("hello_message")
	core.register("A", component)
