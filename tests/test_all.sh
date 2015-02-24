#! /usr/bin/env bash

set -e -o pipefail; 

snakemake -s ../smbl/fasta.snake
snakemake -s ../smbl/prog.snake
