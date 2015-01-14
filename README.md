# Snakemake-lib

## Documentation

**Snakemake-lib** is a library of some useful rules and Python functions which can be used in bioinformatics Snakemake (https://bitbucket.org/johanneskoester/snakemake/) pipelines. Files should be included using
```include: "snakemake-lib/include_all.snake.py"```.

 * **constants.py** - constants for program names, selected fasta files, etc.

 * **progs.snake.py** - rules for downloading and compilation programs.
    
    **Programs** (listed in alphabetical order together with variables with pathes):
    * *art_454* - ```PROG_ART_454```
    * *art_illumina* - ```PROG_ART_ILLUMINA```
    * *art_solid* - ```PROG_ART_SOLID```
    * *bcftools* - ```PROG_BCFTOOLS```
    * *bgzip* - ```PROG_BGZIP```
    * *bwa* - ```PROG_BWA```
    * *dwgsim* - ```PROG_DWGSIM```
    * *samtools* - ```PROG_SAMTOOLS```
    * *tabix* - ```PROG_TABIX```
    
    Defaultly, all the programs are installed into *bin* subdirectory of the script's directory. It is possible to change it by providing a line ```USE_HOME=1``` in *Snakefile* before the including command.

    All functionality of the file can be tested using
    ```bash
    snakemake -s snakemake-lib/progs.snake.py
    ```

 * **fasta.snake.py** - rules for downloading and compilation programs.

    **Data files**
    * ```FA_EXAMPLE``` - an example Fasta file
    
    All functionality of the file can be tested using
    ```bash
    snakemake -s snakemake-lib/progs.snake.py
    ```
## Example

First do clone this repository:
```bash
git clone --depth 1 http://github.com/karel-brinda/snakemake-lib/
```

Then create this simple *Snakefile*:
```python
USE_HOME=1

include: "snakemake-lib/include_all.snake.py"

rule all:
        input:
                DWGSIM,
                BWA,
                EXAMPLE_FASTA
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
 2. DwgSim and BWA are downloaded, compiled and installed
 3. DwgSim simulates reads from the example Fasta file
 4. These reads are mapped back to the reference by BWA (*alignment.sam* is created)
