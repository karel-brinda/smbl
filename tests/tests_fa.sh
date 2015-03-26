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
echo "                 TEST: FASTA files download" 
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
	cd "$(dirname '$0')"
	snakemake -s Snakefile.all_fastas -p
)

(
	set -ex -o pipefail; 

	rm -fR ~/.smbl
	cd "$(dirname '$0')"
	snakemake -s Snakefile.own_fasta -p
)
