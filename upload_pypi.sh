#! /usr/bin/env bash

set -e

cd "$(dirname "$0")"
/usr/bin/env python3 setup.py register sdist upload
