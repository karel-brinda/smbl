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
	verbosity=False

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
	def shell(cls,command):
		if cls.verbosity:
			snakemake.shell(command)
		else:
			snakemake.shell("({}) > /dev/null".format(command))
		
	@classmethod
	def set_verbosity(cls,verbosity):
		cls.verbosity=verbosity		

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
		cls.shell('rm -fR "{src_dir}"'.format(src_dir=cls.src_dir))
		cls.shell('mkdir -p "{src_dir}"'.format(src_dir=cls.src_dir))

	@classmethod
	# fixme: abstract
	def install(cls):
		raise NotImplementedError()

	@classmethod
	def install_post(cls):
		cls.shell('rm -fR "{src_dir}"'.format(src_dir=cls.src_dir))

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
		cls.shell('mkdir -p "{dir}"'.format(dir=dirname_full))
		cls.shell('git clone --recursive --depth 1 "{rep}" "{dir}"'.format(rep=repository,dir=dirname_full))
		return dirname_full

	@classmethod
	def svn_checkout(cls,repository,dirname_short):
		cls.status_message("Cloning a SVN repository: "+repository)
		dirname_full=cls.abs_from_short(dirname_short)
		cls.shell('mkdir -p "{dir}"'.format(dir=dirname_full))
		cls.shell('git svn clone "{rep}" "{dir}"'.format(rep=repository,dir=dirname_full))
		return dirname_full

	@classmethod
	def download_file(cls,address,filename_short):
		cls.status_message("Downloading a file: "+address)
		filename_full=cls.abs_from_short(filename_short)
		cls.shell('mkdir -p "{dir}"'.format(dir=os.path.dirname(filename_full)))
		try:
			cls.shell('curl -L --insecure -o "{fn}" "{address}"'.format(fn=filename_full,address=address))
		except:
			cls.shell('curl -L --insecure -o "{fn}" "{address}"'.format(fn=filename_full,address=address))
		return filename_full

	@classmethod
	def install_file(cls,filename_short,dest,executable=True):
		cls.status_message("Copying: "+cls.abs_from_short(filename_short))
		filename_full=cls.abs_from_short(filename_short)
		cls.shell('cp "{source}" "{dest}"'.format(source=filename_full,dest=dest))
		if executable:
			cls.shell('chmod +x "{}"'.format(dest))

	@classmethod
	def extract_tar(cls,filename_short,strip=0):
		cls.status_message("Extracting an archive: "+cls.abs_from_short(filename_short))
		filename_full=cls.abs_from_short(filename_short)
		dirname_full=os.path.dirname(filename_full)
		cls.shell('cd "{dir}" && tar --strip-component="{strip}" -xf "{fn}"'.format(dir=dirname_full,strip=strip,fn=filename_full))
		return dirname_full

	@classmethod
	def run_make(cls,dirname_short,clean=False,parallel=True):
		cls.status_message("Running make: "+cls.abs_from_short(dirname_short))
		try:
			cls._run_make(dirname_short=dirname_short,clean=clean,parallel=parallel)
		except:
			cls._run_make(dirname_short=dirname_short,clean=False,parallel=False)


	@classmethod
	def _run_make(cls,dirname_short,clean=False,parallel=True):
		dirname_full=cls.abs_from_short(dirname_short)
		other_args=""
		if clean:
			cls.shell('cd "{build_dir}" && make clean'.format(build_dir=dirname_full))
		if parallel:
			other_args+=" --jobs"
		cls.shell('cd "{build_dir}" && make {other_args}'.format(build_dir=dirname_full,other_args=other_args))

	@classmethod
	def run_cmake(cls,dirname_short):
		cls.status_message("Running cmake: "+cls.abs_from_short(dirname_short))
		dirname_full=cls.abs_from_short(dirname_short)
		cls.shell('cd "{build_dir}" && cmake .'.format(build_dir=dirname_full))

	@classmethod
	def run_configure(cls,dirname_short):
		cls.status_message("Running configure: "+cls.abs_from_short(dirname_short))
		dirname_full=cls.abs_from_short(dirname_short)
		cls.shell('cd "{build_dir}" && ./configure'.format(build_dir=dirname_full))

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



