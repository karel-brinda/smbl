#! /usr/bin/env bash
snakemake -s ../smbl/fasta.snake --cores
snakemake -s ../smbl/prog.snake --cores
