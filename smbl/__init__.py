import os
import sys
import snakemake
import platform

import smbl.messages

smbl.messages.message("",program="SMBL")
smbl.messages.message("SnakeMake Bioinformatics Library",program="SMBL")
smbl.messages.message("Web:    http://github.com/karel-brinda/smbl",program="SMBL")
smbl.messages.message("Author: Karel Brinda, karel.brinda@gmail.com",program="SMBL")
smbl.messages.message("",program="SMBL")
smbl.messages.message("Platform: {}".format(sys.platform),program="SMBL")
smbl.messages.message("System: {}".format(platform.system()),program="SMBL")
smbl.messages.message("Machine: {}".format(platform.machine()),program="SMBL")
smbl.messages.message("Processor: {}".format(platform.processor()),program="SMBL")
smbl.messages.message("Python version: {}".format(platform.python_version()),program="SMBL")
smbl.messages.message("Python build: {}".format(", ".join(platform.python_build())),program="SMBL")
smbl.messages.message("",program="SMBL")

# mapping wrappers
#  - commands in practise:
#       - https://github.com/lh3/mem-paper/blob/master/eval/time.txt
#       - http://lh3lh3.users.sourceforge.net/alnROC.shtml

smbl_dir = os.path.join(os.path.expanduser("~"),".smbl")

bin_dir  = os.path.join(smbl_dir,"bin")
fa_dir   = os.path.join(smbl_dir,"fa")
src_dir  = os.path.join(smbl_dir,"src")

import smbl.fasta
import smbl.prog

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

snakemake.shell(
		"""
			mkdir -p "{}" "{}" "{}"
		""".format(bin_dir,fa_dir,src_dir)
	)

def is_linux():
	return sys.platform.startswith('linux')

def is_cygwin():
	return sys.platform.startswith('cygwin')

def is_windows():
	return sys.platform.startswith('win')

def is_osx():
	return sys.platform.startswith('darwin')

def is_os_64bit():
	return platform.machine().endswith('64')

def get_platform():
	if is_linux():
		return "linux"
	if is_windows():
		return "windows"
	if is_osx():
		return "osx"
	if is_cygwin():
		return "cygwin"
