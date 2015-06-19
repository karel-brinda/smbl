#! /usr/bin/env bash

set -e

cd "$(dirname "$0")"
rm -fR build dist SMBL.egg-info

echo
echo
echo "   TEST"
echo
echo

python3 setup.py check

echo
echo
echo "   INSTALLATION"
echo
echo

python3 setup.py install
