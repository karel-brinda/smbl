import smbl
import os

from .clean import *
from .rule import *
from .shell import *
from .platforms import *

def mkdir(directory_fn):
	os.makedirs(directory_fn,exist_ok=True)

def rmdir(directory_fn):
	shutil.rmtree(cls.src_dir,ignore_errors=True)

