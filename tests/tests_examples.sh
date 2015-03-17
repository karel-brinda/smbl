#! /usr/bin/env bash

echo
echo
echo
echo
echo
echo
echo "===================================================================="
echo
echo
echo
echo "                 TEST: examples" 
echo
echo
echo
echo "===================================================================="
echo
echo
echo

(
	set -ex -o pipefail; 

	rm -fR ~/.smbl
	cd "$(dirname "$0")"
	snakemake -p -s ../examples/Snakefile
)
