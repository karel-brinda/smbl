import os
import sys
import platform

import smbl.messages

# mapping wrappers
#  - commands in practise:
#       - https://github.com/lh3/mem-paper/blob/master/eval/time.txt
#       - http://lh3lh3.users.sourceforge.net/alnROC.shtml

try:
	import pkg_resources
	version=pkg_resources.get_distribution("smbl").version
except:
	version="unknown"

smbl.messages.message("",program="SMBL")
smbl.messages.message("SnakeMake Bioinformatics Library",program="SMBL")
smbl.messages.message("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",program="SMBL")
smbl.messages.message("Version: {}".format(version),program="SMBL")
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

smbl_dir = os.path.join(os.path.expanduser("~"),".smbl")

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

smbl.utils.shell(
		"""
			mkdir -p "{}" "{}" "{}"
		""".format(bin_dir,fa_dir,src_dir)
	)
