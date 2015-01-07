# snakemake-lib

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
    
