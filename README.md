# SMBL - SnakeMake Bioinformatics Library

In case of any problem, don't hesitate to contact me on karel.brinda@gmail.com.

## Short description

**SMBL** is a library of some useful rules and Python functions which can be used in Snakemake (https://bitbucket.org/johanneskoester/snakemake/) pipelines. It makes possible to automatically
download various bioinformatics programs like read mappers, read simulators, conversion tools, etc.
It supports also downloading and conversion of some important references in FASTA format (e.g., human genome).

## Installation / upgrade

To install SMBL, you need to have Unix-like operating system (e.g., Linux, MacOS) and Python at least 3.2.
Installation / upgrade can be performed using the following command.

```bash
pip install --upgrade smbl
```

If SnakeMake has not been installed, yet, it will
be installed automatically with SMBL.

The current GIT version of SMBL can be installed by 
```bash
git clone --depth 1 http://github.com/karel-brinda/smbl
cd smbl
./install.sh
```

## Usage

To use SMBL, you have to import the *smbl*  Python package and include a file with all rules using:
```python
import smbl
include: smbl.include
```

Then you can use all supported programs or data. When they appear as input of a rule, they will be downloaded or compiled.

All the programs are installed into ```~/.smbl/bin/``` and all FASTA files into ```~/.smbl/fa/```.


### Programs

| Program          | Variable with its filename          | Link |
|------------------|-------------------------------------|------|
| art\_454         | ```smbl.prog.ART_454```             | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
| art\_illumina    | ```smbl.prog.ART_ILLUMINA```        | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
| art\_solid       | ```smbl.prog.ART_SOLID```           | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
| bcftools         | ```smbl.prog.BCFTOOLS```            | http://github.com/samtools/bcftools |
| bfast            | ```smbl.prog.BFAST```               | http://github.com/nh13/bfast |
| bgzip            | ```smbl.prog.BGZIP```               | http://github.com/samtools/htslib
| bwa              | ```smbl.prog.BWA```                 | http://github.com/lh3/bwa |
| dwgsim           | ```smbl.prog.DWGSIM```              | http://github.com/nh13/dwgsim |
| dwgsim\_eval     | ```smbl.prog.DWGSIM_EVAL```         | http://github.com/nh13/dwgsim |
| drfast           | ```smbl.prog.DRFAST```              | http://github.com/BilkentCompGen/drfast |
| freec            | ```smbl.prog.FREEC```               | http://bioinfo-out.curie.fr/projects/freec/ |
| gem-indexer      | ```smbl.prog.GEM_INDEXER```         | http://algorithms.cnag.cat/wiki/The_GEM_library |
| gem-mapper       | ```smbl.prog.GEM_MAPPER```          | http://algorithms.cnag.cat/wiki/The_GEM_library |
| gem-2-sam        | ```smbl.prog.GEM_2_SAM```           | http://algorithms.cnag.cat/wiki/The_GEM_library |
| mason            | ```smbl.prog.MASON```               | http://github.com/seqan/seqan |
| mrfast           | ```smbl.prog.MRFAST```              | http://github.com/BilkentCompGen/mrfast |
| mrsfast          | ```smbl.prog.MRSFAST```             | http://mrsfast.sourceforge.net/ |
| perm             | ```smbl.prog.PERM```                | http://code.google.com/p/perm/ |
| samtools         | ```smbl.prog.SAMTOOLS```            | http://github.com/samtools/samtools |
| sirfast          | ```smbl.prog.SIRFAST```             | http://github.com/BilkentCompGen/sirfast |
| storm-color      | ```smbl.prog.STORM_COLOR```         | http://bioinfo.lifl.fr/yass/iedera_solid/storm/ |
| storm-nucleotide | ```smbl.prog.STORM_NUCLEOTIDE```    | http://bioinfo.lifl.fr/yass/iedera_solid/storm/ |
| tabix            | ```smbl.prog.TABIX```               | http://github.com/samtools/htslib |
| twoBitToFa       | ```smbl.prog.TWOBITTOFA```          | http://hgdownload.cse.ucsc.edu/admin/exe/ |
| wgsim            | ```smbl.prog.WGSIM```               | http://github.com/lh3/wgsim |
| wgsim\_eval.pl   | ```smbl.prog.WGSIM_EVAL```          | http://github.com/lh3/wgsim |
    

### FASTA files

| FASTA file                   | Variable with its filename   |
|------------------------------|------------------------------|
| An example small FASTA file  | ```smbl.fasta.EXAMPLE```     |
| Human genome HG38 (GRCh38)   | ```smbl.fasta.HG38```, ```smbl.fasta.HUMAN_GRCH38 ``` |

## Example

Try to create this simple *Snakefile*:
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

 1. An example FASTA file is downloaded
 2. DwgSim and BWA are downloaded, compiled and installed
 3. DwgSim simulates reads from the example Fasta file
 4. These reads are mapped back to the reference by BWA (*alignment.sam* is created)
