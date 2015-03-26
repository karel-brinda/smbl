#! /usr/bin/env bash

set -e

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
echo "                 TEST: multi-threading installation" 
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
	snakemake -s Snakefile.all_programs -p --cores 8
)
