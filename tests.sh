#! /usr/bin/env bash

set -e -o pipefail; 


echo "Test normal" 

rm -fR ~/.sbml

snakemake -s ./smbl/prog.snake
snakemake -s ./smbl/fasta.snake

echo "Test parallel"

rm -fR ~/.sbml

snakemake -s ./smbl/prog.snake --cores
snakemake -s ./smbl/fasta.snake --cores
