#! /usr/bin/env bash

set -e -o pipefail; 

cd tests

./clean_files.sh
./test_all.sh
./clean_files.sh
./test_all_cores.sh
./clean_files.sh
