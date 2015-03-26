#! /usr/bin/env bash

cd "$(dirname '$0')"
rm -fR build dist SMBL.egg-info
python3 setup.py install
