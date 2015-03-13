import snakemake
import smbl
import collections
import random
import os

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

def get_bin_file_path(program):
	return os.path.join(smbl.bin_dir,program)


##########################################
##########################################


class ProgramWatcher(type):
	def __init__(cls, name, bases, clsdict):
		if len(cls.mro()) == 3:
			register_plugin(cls)
			cls.src_dir=os.path.join(smbl.src_dir,cls.__name__)
		super(ProgramWatcher, cls).__init__(name, bases, clsdict)


class Program(metaclass = ProgramWatcher):
	src_dir=""

	def __init__(self):
		pass

	@classmethod
	def install_all_steps(cls):
		cls.install_pre()
		cls.install()
		cls.install_post()

	@classmethod
	def install_pre(cls):
		smbl.snakemake('rm -fR "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))
		smbl.snakemake('mkdir -p "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))

	@classmethod
	# fixme: abstract
	def install(cls):
		pass		

	@classmethod
	def install_post(cls):
		smbl.snakemake('rm -fR "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))

	@classmethod
	# fixme: abstract
	def supported_platforms(cls):
		pass

	@classmethod
	# fixme: abstract
	def get_installation_files(cls):
		pass

	@classmethod
	def git_clone(cls,repository,dirname):
		directory_full=os.path.join(cls.src_dir,dirname)
		snakemake.shell('mkdir -p "{dir}" > /dev/null'.format(dir=directory_full))
		snakemake.shell('git clone --recursive --depth 1 "{rep}" "{dir}" > /dev/null'.format(rep=repository,dir=directory_full))

	@classmethod
	def install_file(cls,source,dest):
		filename_full=os.path.join(cls.src_dir,source)
		snakemake.shell('cp "{source}" "{dest}" > /dev/null'.format(source=filename_full,dest=dest))

	@classmethod
	def get_priority(cls):
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



