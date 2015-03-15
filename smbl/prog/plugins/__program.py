import snakemake
import smbl
import collections
import random
import os
import abc

from termcolor import colored, cprint

__PLUGINS = set()
__RULES= set()

def register_plugin(plugin):
	__PLUGINS.add(plugin)

def get_registered_plugins():
	return list(__PLUGINS)

def register_rule(rule):
	__RULES.add(rule)

def get_registered_rules():
	return list(__RULES)

def get_bin_file_path(program):
	return os.path.join(smbl.bin_dir,program)


##########################################
##########################################


#class ProgramWatcher(abc.ABCMeta):
class ProgramWatcher(type):
	def __init__(cls,name,bases,clsdict):
		if len(cls.mro()) == 3:
			register_plugin(cls)
			cls.src_dir=os.path.join(smbl.src_dir,cls.__name__)
		super(ProgramWatcher, cls).__init__(name, bases, clsdict)


class Program(metaclass=ProgramWatcher):
	src_dir=""

	def __init__(self):
		pass

	@classmethod
	def status_message(cls,message):
		cprint(
			"[SMBL] '{}': {}".format(cls.__name__,message),
			"blue",
			#"on_black",
			attrs=['bold'],
		)

		

	@classmethod
	def install_all_steps(cls):
		cls.status_message("Installation started")
		cls.install_pre()
		cls.install()
		cls.install_post()
		cls.status_message("Installation completed")

	@classmethod
	def install_pre(cls):
		assert len(set(cls.supported_platforms()))>0, ""
		assert set(cls.supported_platforms()).issubset(smbl.prog.all_platforms)
		if not cls.is_platform_supported():
			raise NotImplementedError("This platform is not supported ({})".format(smbl.get_platform()))
		snakemake.shell('rm -fR "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))
		snakemake.shell('mkdir -p "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))

	@classmethod
	# fixme: abstract
	def install(cls):
		raise NotImplementedError()

	@classmethod
	def install_post(cls):
		snakemake.shell('rm -fR "{src_dir}" > /dev/null'.format(src_dir=cls.src_dir))

	@classmethod
	# fixme: abstract
	def supported_platforms(cls):
		raise NotImplementedError()

	@classmethod
	def is_platform_supported(cls):
		platform=smbl.get_platform()
		if platform in cls.supported_platforms():
			return True
		else:
			return False

	@classmethod
	# fixme: abstract
	def get_installation_files(cls):
		raise NotImplementedError()

	@classmethod
	def git_clone(cls,repository,dirname_short):
		cls.status_message("Cloning a GIT repository: "+repository)
		dirname_full=cls.abs_from_short(dirname_short)
		snakemake.shell('mkdir -p "{dir}" > /dev/null'.format(dir=dirname_full))
		snakemake.shell('git clone --recursive --depth 1 "{rep}" "{dir}" > /dev/null'.format(rep=repository,dir=dirname_full))
		return dirname_full

	@classmethod
	def svn_checkout(cls,repository,dirname_short):
		cls.status_message("Cloning a SVN repository: "+repository)
		dirname_full=cls.abs_from_short(dirname_short)
		snakemake.shell('mkdir -p "{dir}" > /dev/null'.format(dir=dirname_full))
		snakemake.shell('git svn clone "{rep}" "{dir}" > /dev/null'.format(rep=repository,dir=dirname_full))
		return dirname_full

	@classmethod
	def download_file(cls,address,filename_short):
		cls.status_message("Downloading a file: "+address)
		filename_full=cls.abs_from_short(filename_short)
		snakemake.shell('mkdir -p "{dir}" > /dev/null'.format(dir=os.path.dirname(filename_full)))
		snakemake.shell('curl -L --insecure -o "{fn}" "{address}"'.format(fn=filename_full,address=address))
		return filename_full

	@classmethod
	def install_file(cls,filename_short,dest,executable=True):
		cls.status_message("Copying: "+cls.abs_from_short(filename_short))
		filename_full=cls.abs_from_short(filename_short)
		snakemake.shell('cp "{source}" "{dest}" > /dev/null'.format(source=filename_full,dest=dest))
		if executable:
			snakemake.shell('chmod +x "{}" > /dev/null'.format(dest))

	@classmethod
	def extract_tar(cls,filename_short,strip=0):
		cls.status_message("Extracting an archive: "+cls.abs_from_short(filename_short))
		filename_full=cls.abs_from_short(filename_short)
		dirname_full=os.path.dirname(filename_full)
		snakemake.shell('(cd "{dir}" && tar --strip-component="{strip}" -xf "{fn}") > /dev/null'.format(dir=dirname_full,strip=strip,fn=filename_full))
		return dirname_full

	@classmethod
	def run_make(cls,dirname_short,clean=False,parallel=True):
		cls.status_message("Running make: "+cls.abs_from_short(dirname_short))
		dirname_full=cls.abs_from_short(dirname_short)
		if clean:
			snakemake.shell('(cd "{build_dir}" && make clean) > /dev/null'.format(build_dir=dirname_full))
		other_args=""
		if parallel:
			other_args+=" --jobs"
		snakemake.shell('(cd "{build_dir}" && make {other_args}) > /dev/null'.format(build_dir=dirname_full,other_args=other_args))

	@classmethod
	def run_cmake(cls,dirname_short):
		cls.status_message("Running cmake: "+cls.abs_from_short(dirname_short))
		dirname_full=cls.abs_from_short(dirname_short)
		snakemake.shell('(cd "{build_dir}" && cmake .) > /dev/null'.format(build_dir=dirname_full))

	@classmethod
	def run_configure(cls,dirname_short):
		cls.status_message("Running configure: "+cls.abs_from_short(dirname_short))
		dirname_full=cls.abs_from_short(dirname_short)
		snakemake.shell('(cd "{build_dir}" && ./configure) > /dev/null'.format(build_dir=dirname_full))

	@classmethod
	def get_priority(cls):
		__installation_priority=random.randint(1,10000000)
		return __installation_priority

	@classmethod
	def abs_from_short(cls,short):
		return os.path.abspath(os.path.join(cls.src_dir,short))



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
		return self.__priority



