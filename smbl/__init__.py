import os
import sys
import snakemake
import platform

# todo: mapping wrappers
#  - commands in practise:
#       - https://github.com/lh3/mem-paper/blob/master/eval/time.txt
#       - http://lh3lh3.users.sourceforge.net/alnROC.shtml

smbl_dir = os.path.join(os.path.expanduser("~"),".smbl")

bin_dir  = os.path.join(smbl_dir,"bin")
fa_dir   = os.path.join(smbl_dir,"fa")
src_dir  = os.path.join(smbl_dir,"src")

import smbl.fasta
import smbl.prog
#import smbl.prog.plugins

def include():
	return os.path.join(
			os.path.dirname(__file__),
			"include_all.snake"
		)

def all_programs():
	return [plugin.get_installation_files() for plugin in smbl.prog.plugins.get_registered_plugins()]

def all_installable_programs():
	return

snakemake.shell(
		"""
			mkdir -p "{}" "{}" "{}"
		""".format(bin_dir,fa_dir,src_dir)
	)

def run_commands(commands, verbose=False):
	for command in commands.split(os.linesep):
		command = command.strip()
		if command == "":
			continue
		if verbose==False:
			command = "({})>/dev/null".format(command)
		snakemake.shell(command)

def is_linux():
	return sys.platform.startswith('linux')

def is_cygwin():
	return sys.platform.startswith('cygwin')

def is_windows():
	return sys.platform.startswith('win')

def is_mac():
	return sys.platform.startswith('darwin')

def is_os_64bit():
	return platform.machine().endswith('64')

def get_platform():
	if is_linux():
		return "linux"
	if is_windows():
		return "windows"
	if is_mac():
		return "macos"
	if is_cygwin():
		return "cygwin"
