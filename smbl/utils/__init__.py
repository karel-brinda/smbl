import smbl
import sys
import platform
import snakemake
import re

from .clean import *
from .rule import *

def shell(
			cmd,
			remove_spaces=True
		):
	if remove_spaces:
		#print("removing spaces from command")
		cmd=re.sub(r'[ \t\f\v]+',' ',cmd).strip()

	return snakemake.shell(cmd)

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
