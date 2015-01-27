# SMBL - SnakeMake Bioinformatics Library

## Installation
```bash
pip install --upgrade smbl
```

## Usage

**SMBL** is a library of some useful rules and Python functions which can be used in bioinformatics Snakemake (https://bitbucket.org/johanneskoester/snakemake/) pipelines. Files should be included using
```python
import smbl
include: smbl.include
```.

 * Programs:
    
    **Programs** (listed in alphabetical order together with variables with pathes):
    * *art_454* - ```smbl.prog.ART_454```
    * *art_illumina* - ```smbl.prog.ART_ILLUMINA```
    * *art_solid* - ```smbl.prog.ART_SOLID```
    * *bcftools* - ```smbl.prog.BCFTOOLS```
    * *bgzip* - ```smbl.prog.BGZIP```
    * *bwa* - ```smbl.prog.BWA```
    * *dwgsim* - ```smbl.prog.DWGSIM```
    * *samtools* - ```smbl.prog.SAMTOOLS```
    * *tabix* - ```smbl.prog.TABIX```
    
    Defaultly, all the programs are installed into ~/.smbl/bin/.


 * Fasta:

    * ```smbl.fasta.EXAMPLE``` - an example Fasta file

## Example

Then create this simple *Snakefile*:
```python
import smbl
include: smbl.include

rule all:
        input:
                smbl.prog.DWGSIM,
                smbl.prog.BWA,
                smbl.fasta.EXAMPLE
        params:
                PREF="simulated_reads",
                INDEX="bwa_index"
        output:
                "alignment.sam"
        run:
                shell("{input[0]} -C 1 {input[2]} {params.PREF}")
                shell("{input[1]} index {input[2]}")
                shell("{input[1]} mem {input[2]} {params.PREF}.bfast.fastq > alignment.sam")
```

Run the script.
```bash
snakemake
```

What happens:

 1. An example Fasta is downloaded
 2. DwgSim and BWA are downloaded, compiled and installed into ```~/.smbl/bin```
 3. DwgSim simulates reads from the example Fasta file
 4. These reads are mapped back to the reference by BWA (*alignment.sam* is created)
