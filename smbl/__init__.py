import os
import sys
import snakemake
import platform

bin_dir = os.path.join(os.path.expanduser("~"),".smbl","bin")
fa_dir = os.path.join(os.path.expanduser("~"),".smbl","fa")
src_dir = os.path.join(os.path.expanduser("~"),".smbl","src")

from smbl.rnf import *
import smbl.fasta
import smbl.prog

include = os.path.join( os.path.dirname(__file__), "include_all.snake")




print("directory for programs: ",bin_dir, file=sys.stderr)
print("directory for fasta files: ",fa_dir, file=sys.stderr)
print("directory for source codes: ",src_dir, file=sys.stderr)

snakemake.shell("mkdir -p {} {} {}".format(bin_dir,fa_dir,src_dir))


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

