import os
import builtins

import smbl.messages

# mapping wrappers
#  - commands in practise:
#       - https://github.com/lh3/mem-paper/blob/master/eval/time.txt
#       - http://lh3lh3.users.sourceforge.net/alnROC.shtml


import sys

try:
	import pkg_resources
	__version__=pkg_resources.get_distribution("smbl").version
except:
	__version__=""

DEFAULT_SMBL_CONF = {
		# print information about SMBL during import
		'print_info': sys.argv[0]=="snakemake",
		# directory where SMBL installs all data and programs
		'directory': os.path.join(os.path.expanduser("~"),".smbl"),
		# create the directory when SMBL is imported
		'ensure_directory': True,
	}

try:
	SMBL_CONF = builtins.SMBL_CONF
except:
	SMBL_CONF = {}

assert type(SMBL_CONF) is dict, "builtins.SMBL_CONF must be a dictionary"
for key in DEFAULT_SMBL_CONF.keys():
	if not key in SMBL_CONF:
		SMBL_CONF[key]=DEFAULT_SMBL_CONF[key]

#print("SMBL configuration:",SMBL_CONF)

if SMBL_CONF["print_info"]:
	import platform
	import sys

	smbl.messages.message("",program="SMBL")
	smbl.messages.message("SnakeMake Bioinformatics Library",program="SMBL")
	smbl.messages.message("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",program="SMBL")
	smbl.messages.message("Version: {}".format(__version__),program="SMBL")
	smbl.messages.message("Web:     http://github.com/karel-brinda/smbl",program="SMBL")
	smbl.messages.message("Contact: Karel Brinda, karel.brinda@univ-mlv.fr",program="SMBL")
	smbl.messages.message("",program="SMBL")
	smbl.messages.message("Platform: {}".format(sys.platform),program="SMBL")
	smbl.messages.message("System: {}".format(platform.system()),program="SMBL")
	smbl.messages.message("Machine: {}".format(platform.machine()),program="SMBL")
	smbl.messages.message("Processor: {}".format(platform.processor()),program="SMBL")
	smbl.messages.message("Python version: {}".format(platform.python_version()),program="SMBL")
	smbl.messages.message("Python build: {}".format(", ".join(platform.python_build())),program="SMBL")
	smbl.messages.message("",program="SMBL")

smbl_dir = SMBL_CONF["directory"]
bin_dir  = os.path.join(smbl_dir,"bin")
fa_dir   = os.path.join(smbl_dir,"fa")
src_dir  = os.path.join(smbl_dir,"src")

import smbl.utils
import smbl.prog
import smbl.fasta

def include():
	return os.path.join(
			os.path.dirname(__file__),
			"include_all.snake"
		)

def all_fastas():
	return [
			fastafile.get() for fastafile in smbl.fasta.get_registered_fastas()
		]

def all_programs():
	return [
			plugin.get_installation_files() for plugin in smbl.prog.plugins.get_registered_plugins()
		]

def all_compatible_programs():
	return [
			plugin.get_installation_files() for plugin in smbl.prog.plugins.get_registered_plugins()
				if plugin.is_platform_supported()
		]

if SMBL_CONF["ensure_directory"]:
	smbl.utils.shell(
			"""
				mkdir -p "{}" "{}" "{}"
			""".format(bin_dir,fa_dir,src_dir)
		)
