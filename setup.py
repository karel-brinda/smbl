#!/usr/bin/env python

import setuptools

SKIP_GENERATE_AUTHORS=1
SKIP_WRITE_GIT_CHANGELOG=1

setuptools.setup(
	setup_requires=['pbr'],
	pbr=True,
)
