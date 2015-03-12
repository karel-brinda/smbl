import snakemake
import smbl
import collections
import random

__PLUGINS = set()
__RULES= set()

def register_plugin(plugin):
	print("registering plugin",plugin)
	__PLUGINS.add(plugin)

def get_registered_plugins():
	return list(__PLUGINS)

def register_rule(rule):
	print("registering rule",rule)
	__RULES.add(rule)

def get_registered_rules():
	return list(__RULES)


##########################################
##########################################


class ProgramWatcher(type):
	def __init__(cls, name, bases, clsdict):
		if len(cls.mro()) == 3:
			register_plugin(cls)
		super(ProgramWatcher, cls).__init__(name, bases, clsdict)


class Program(metaclass = ProgramWatcher):
	def __init__(self):
		pass

	@staticmethod
	def install(directory):
		pass

	@staticmethod
	def supported_platforms():
		pass

	@staticmethod
	def get_files():
		pass

	@staticmethod
	def get_priority():
		__installation_priority=random.randint(1,10000000)
		print ("install. priority",__installation_priority)
		return __installation_priority


##########################################
##########################################


class Rule:
	def __init__(self,input,output,run):
		register_rule(self)

		self.__input=input
		self.__output=output
		self.__run=run
		self.__priority=random.randint(1,10000000)

	def get_input(self):
		return self.__input

	def get_output(self):
		return self.__output

	def run(self):
		self.__run()

	def get_priority(self):
		print ("priority",self.__priority)
		return self.__priority



