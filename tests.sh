#! /usr/bin/env bash

echo "===================================================================="
echo
echo
echo
echo "                     Test: single-threading" 
echo
echo
echo
echo "===================================================================="

(
	set -ex -o pipefail; 
	rm -fR ~/.sbml

	snakemake -s ./smbl/prog.snake
	snakemake -s ./smbl/fasta.snake
)

echo "===================================================================="
echo
echo
echo
echo "                     Test: multi-threading" 
echo
echo
echo
echo "===================================================================="

(
	set -ex -o pipefail; 
	rm -fR ~/.sbml

	snakemake -s ./smbl/prog.snake --cores
	snakemake -s ./smbl/fasta.snake --cores
)
