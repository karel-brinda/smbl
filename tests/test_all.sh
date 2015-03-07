#! /usr/bin/env bash

set -e -o pipefail; 

snakemake -s ../smbl/fasta/fasta.snake
snakemake -s ../smbl/prog/prog.snake
