#! /usr/bin/env bash

set -e -o pipefail; 

rm -fR ~/.sbml

snakemake -s ./smbl/prog.snake
snakemake -s ./smbl/fasta.snake

rm -fR ~/.sbml

snakemake -s ./smbl/prog.snake --cores
snakemake -s ./smbl/fasta.snake --cores
