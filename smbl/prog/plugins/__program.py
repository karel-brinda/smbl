import snakemake
import smbl
import collections


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
		if len(cls.mro()) > 2:
			register_plugin(cls)
		super(ProgramWatcher, cls).__init__(name, bases, clsdict)


class Program(metaclass = ProgramWatcher):
	def __init__(self):
		pass
	#	self.rules=[]
	#	smbl.prog.add_program_instance(self)

	@staticmethod
	def install(directory):
		pass

	@staticmethod
	def supported_platforms():
		pass

	@staticmethod
	def get_files():
		pass

	def run_commands(commands):
		for command in commands.split(os.linesep):
			command = command.strip()
			if command == "":
				continue
			snakemake.shell(command)


##########################################
##########################################


class Rule:
	def __init__(self,input,output,run):
		register_rule(self)

		self.__input=input
		self.__output=output
		self.__run=run

	def get_input(self):
		return self.__input

	def get_output(self):
		return self.__output

	def run(self):
		self.__run()


