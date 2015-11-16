import smbl
import os
import shutil

from .clean import *
from .rule import *
from .shell import *
from .platforms import *

def mkdir(directory_fn):
	os.makedirs(directory_fn,exist_ok=True)

def rmdir(directory_fn):
	shutil.rmtree(directory_fn,ignore_errors=True)

