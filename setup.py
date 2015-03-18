import sys
import setuptools

from pbr import util

setuptools.setup(
	**util.cfg_to_args()
)
