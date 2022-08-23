class Hello():
	def __init__(self,name):
		self._name=name
	def say_hello(self):
		print("Hello World!")
hello1=Hello("张三")
hello1.say_hello()