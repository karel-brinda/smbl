#! /usr/bin/env bash

set -e -o pipefail; 

snakemake -s ../smbl/prog/prog.snake --cores
snakemake -s ../smbl/fasta/fasta.snake --cores

