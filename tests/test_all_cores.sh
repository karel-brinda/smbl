#! /usr/bin/env bash

set -e -o pipefail; 

snakemake -s ../smbl/fasta.snake --cores
snakemake -s ../smbl/prog.snake --cores
