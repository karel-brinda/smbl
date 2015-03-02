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
echo "                 TEST: single-threading installation" 
echo
echo
echo
echo "===================================================================="

(
	set -ex -o pipefail; 
	rm -fR ~/.smbl

	snakemake -s ./smbl/prog.snake
	snakemake -s ./smbl/fasta.snake
)

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

(
	set -ex -o pipefail; 
	rm -fR ~/.smbl

	snakemake -s ./smbl/prog.snake --cores
	snakemake -s ./smbl/fasta.snake --cores
)
