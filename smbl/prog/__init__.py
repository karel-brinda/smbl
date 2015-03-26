import os
import smbl
import smbl.prog.plugins

all_platforms = ["linux","windows","osx","cygwin"]

from smbl.prog.plugins import *

def correct_samtools_make(makefile_fn):
	makefile_backup_fn = makefile_fn+".backup"
	if not os.path.isfile(makefile_backup_fn):
		with open(makefile_fn, 'r') as makefile:
			content = makefile.read()
			if smbl.is_linux():
				content = content.replace("-lcurses","-lncurses")
			elif smbl.is_cygwin():
				content = content.replace("-D_FILE_OFFSET_BITS=64","-D_FILE_OFFSET_BITS=64 -Dexpl=exp -Dlogl=log")
		with open(makefile_fn, 'w') as makefile:
			makefile.write(content)
