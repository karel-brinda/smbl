import pkgutil
import inspect

from ._program import *

from .art import *
from .bcftools import *
from .bfast import *
from .bowtie import *
from .bwa import *
from .cmake import *
from .curesim import *
from .deez import *
from .drfast import *
from .dwgsim import *
from .freec import *
from .gem import *
from .gnuplot import *
from .htslib import *
from .kallisto import *
from .last import *
from .mrfast import *
from .mrsfast import *
from .pbsim import *
from .perm import *
from .picard import *
from .sambamba import *
from .samtools import *
from .seqan import *
from .sirfast import *
from .storm import *
from .twobittofa import *
from .wgsim import *
from .xs import *



#for loader, name, is_pkg in pkgutil.walk_packages(__path__):
#	module = loader.find_module(name).load_module(name)
#
#	for name, value in inspect.getmembers(module):
#		if name.startswith('__'):
#			continue
#
#		globals()[name] = value
#		__all__.append(name)

