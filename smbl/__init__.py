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

from smbl.rnf import *
import smbl.fasta
import smbl.prog

include = os.path.join( os.path.dirname(__file__), "include_all.snake")

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

def is_mac():
	return sys.platform.startswith('darwin')

def is_os_64bit():
    return platform.machine().endswith('64')

