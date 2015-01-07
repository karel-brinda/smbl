# Snakemake-lib

## Documentation

**Snakemake-lib** is a library of some useful rules and Python functions which can be used in bioinformatics Snakemake (https://bitbucket.org/johanneskoester/snakemake/) pipelines. Files should be included using the ```include:``` command.

 * **progs.py** - rules for downloading and compilation programs and data.
    
    **Programs** (listed in alphabetical order together with variables with pathes):
    * *art_454* - ```ART_454```
    * *art_illumina* - ```ART_ILLUMINA```
    * *art_solid* - ```ART_SOLID```
    * *bcftools* - ```BCFTOOLS```
    * *bgzip* - ```BGZIP```
    * *bwa* - ```BWA```
    * *dwgsim* - ```DWGSIM```
    * *samtools* - ```SAMTOOLS```
    * *tabix* - ```TABIX```
    
    Defaultly, all the programs are installed into *bin* subdirectory of the script's directory. It is possible to change it by providing a line ```USE_HOME=1``` in *Snakefile* before including this file    
    **Data files**
    * ```EXAMPLE_FASTA``` - an example Fasta file ()
    
## Example

First do clone this repository:
```bash
git clone --depth 1 http://github.com/karel-brinda/snakemake-lib/
```

Then create this simple *Snakefile*:
```python
USE_HOME=1

include: "snakemake-lib/progs.py"

rule all:
        input:
                DWGSIM, BWA, EXAMPLE_FASTA
        params:
                DWGSIM=DWGSIM,
                BWA=BWA,
                FASTA=EXAMPLE_FASTA,
                PREF="simulated_reads",
                INDEX="bwa_index"
        output:
                "alignment.sam"
        run:
                shell("{params.DWGSIM} -C 1 {params.FASTA} {params.PREF}")
                shell("{params.BWA} index {params.FASTA}")
                shell("{params.BWA} mem {params.FASTA} {params.PREF}.bfast.fastq > alignment.sam")
```

Run the script.
```bash
snakemake
```

What happens:

 1. An example Fasta is downloaded
 2. DwgSim and BWA are downloaded, compiled and installed
 3. DwgSim simulates reads from the example Fasta file
 4. These reads are mapped back to the reference by BWA (*alignment.sam* is created)
