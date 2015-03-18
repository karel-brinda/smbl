SMBL - SnakeMake Bioinformatics Library
=======================================

.. image:: https://travis-ci.org/karel-brinda/smbl.svg?branch=master
	:target: https://travis-ci.org/karel-brinda/smbl


In case of any problem, don't hesitate to contact me on karel.brinda@gmail.com.


Short description
-----------------

**SMBL** is a library of some useful rules and Python functions which can be used in Snakemake (https://bitbucket.org/johanneskoester/snakemake/) pipelines. It makes possible to automatically
download various bioinformatics programs like read mappers, read simulators, conversion tools, etc.
It supports also downloading and conversion of some important references in FASTA format (e.g., human genome).


Installation / upgrade
----------------------

To install SMBL, you need to have Unix-like operating system (e.g., Linux, MacOS) and Python at least 3.2.
Installation / upgrade can be performed using the following command.

.. code-block:: bash

	pip install --upgrade smbl


If SnakeMake has not been installed, yet, it will
be installed automatically with SMBL.

The current GIT version of SMBL can be installed by 

.. code-block:: bash

	git clone --depth 1 http://github.com/karel-brinda/smbl
	cd smbl
	./install.sh


Usage
-----

To use SMBL, you have to import the *smbl*  Python package and include a file with all rules using:

.. code-block:: python

	import smbl
	include: smbl.include()


Then you can use all supported programs or data. When they appear as input of a rule, they will be downloaded or compiled.

All the programs are installed into ``~/.smbl/bin/`` and all FASTA files into ``~/.smbl/fa/``.


Programs
^^^^^^^^

+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| Program                | Variable with its filename              | Link                                                                    |
+========================+=========================================+=========================================================================+
| art\_454               | ``smbl.prog.ART_454``                   | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| art\_illumina          | ``smbl.prog.ART_ILLUMINA``              | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| art\_solid             | ``smbl.prog.ART_SOLID``                 | http://www.niehs.nih.gov/research/resources/software/biostatistics/art/ |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bcftools               | ``smbl.prog.BCFTOOLS``                  | http://github.com/samtools/bcftools                                     |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bfast                  | ``smbl.prog.BFAST``                     | http://github.com/nh13/bfast                                            |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bgzip                  | ``smbl.prog.BGZIP``                     | http://github.com/samtools/htslib                                       |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bowtie2                | ``smbl.prog.BOWTIE2``                   | http://github.com/BenLangmead/bowtie2                                   |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bowtie2-build          | ``smbl.prog.BOWTIE2_BUILD``             | http://github.com/BenLangmead/bowtie2                                   |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bowtie2-inspect        | ``smbl.prog.BOWTIE2_INSPECT``           | http://github.com/BenLangmead/bowtie2                                   |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| bwa                    | ``smbl.prog.BWA``                       | http://github.com/lh3/bwa                                               |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| curesim.jar            | ``smbl.prog.CURESIM``                   | http://www.pegase-biosciences.com/tools/curesim/                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| curesim_eval.jar       | ``smbl.prog.CURESIM_EVAL``              | http://www.pegase-biosciences.com/tools/curesim/                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| dwgsim                 | ``smbl.prog.DWGSIM``                    | http://github.com/nh13/dwgsim                                           |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| dwgsim\_eval.pl        | ``smbl.prog.DWGSIM_EVAL``               | http://github.com/nh13/dwgsim                                           |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| drfast                 | ``smbl.prog.DRFAST``                    | http://github.com/BilkentCompGen/drfast                                 |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| freec                  | ``smbl.prog.FREEC``                     | http://bioinfo-out.curie.fr/projects/freec/                             |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| gem-indexer            | ``smbl.prog.GEM_INDEXER``               | http://algorithms.cnag.cat/wiki/The_GEM_library                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| gem-mapper             | ``smbl.prog.GEM_MAPPER``                | http://algorithms.cnag.cat/wiki/The_GEM_library                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| gem-2-sam              | ``smbl.prog.GEM_2_SAM``                 | http://algorithms.cnag.cat/wiki/The_GEM_library                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| gnuplot4               | ``smbl.prog.GNUPLOT4``                  | http://www.gnuplot.info/                                                |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| gnuplot5               | ``smbl.prog.GNUPLOT5``                  | http://www.gnuplot.info/                                                |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| lastal                 | ``smbl.prog.LASTAL``                    | http://last.cbrc.jp/                                                    |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| lastdb                 | ``smbl.prog.LASTDB``                    | http://last.cbrc.jp/                                                    |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_frag_sequencing  | ``smbl.prog.MASON_FRAG_SEQUENCING``     | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_genome           | ``smbl.prog.MASON_GENOME``              | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_materializer     | ``smbl.prog.MASON_MATERIALIZER``        | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_methylation      | ``smbl.prog.MASON_METHYLATION``         | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_simulator        | ``smbl.prog.MASON_SIMULATOR``           | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_splicing         | ``smbl.prog.MASON_SPLICING``            | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mason_variator         | ``smbl.prog.MASON_VARIATOR``            | http://packages.seqan.de/mason2/                                        |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mrfast                 | ``smbl.prog.MRFAST``                    | http://github.com/BilkentCompGen/mrfast                                 |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| mrsfast                | ``smbl.prog.MRSFAST``                   | http://mrsfast.sourceforge.net/                                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| perm                   | ``smbl.prog.PERM``                      | http://code.google.com/p/perm/                                          |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| pbsim                  | ``smbl.prog.PBSIM``                     | https://code.google.com/p/pbsim                                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| picard                 | ``smbl.prog.PICARD``                    | http://broadinstitute.github.io/picard/                                 |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| sambamba               | ``smbl.prog.SAMBAMBA``                  | http://lomereiter.github.io/sambamba/                                   |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| samtools               | ``smbl.prog.SAMTOOLS``                  | http://github.com/samtools/samtools                                     |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| sirfast                | ``smbl.prog.SIRFAST``                   | http://github.com/BilkentCompGen/sirfast                                |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| storm-color            | ``smbl.prog.STORM_COLOR``               | http://bioinfo.lifl.fr/yass/iedera_solid/storm/                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| storm-nucleotide       | ``smbl.prog.STORM_NUCLEOTIDE``          | http://bioinfo.lifl.fr/yass/iedera_solid/storm/                         |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| tabix                  | ``smbl.prog.TABIX``                     | http://github.com/samtools/htslib                                       |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| twoBitToFa             | ``smbl.prog.TWOBITTOFA``                | http://hgdownload.cse.ucsc.edu/admin/exe/                               |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| wgsim                  | ``smbl.prog.WGSIM``                     | http://github.com/lh3/wgsim                                             |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| wgsim\_eval.pl         | ``smbl.prog.WGSIM_EVAL``                | http://github.com/lh3/wgsim                                             |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
| xs                     | ``smbl.prog.XS``                        | http://bioinformatics.ua.pt/software/xs/                                |
+------------------------+-----------------------------------------+-------------------------------------------------------------------------+
	

FASTA files
^^^^^^^^^^^

+------------------------------+------------------------------------------------------------+
| FASTA file                   | Variable with its filename                                 |
+==============================+============================================================+
| An example small FASTA file  | ``smbl.fasta.EXAMPLE_1``                                   |
+------------------------------+------------------------------------------------------------+
| An example small FASTA file  | ``smbl.fasta.EXAMPLE_2``                                   |
+------------------------------+------------------------------------------------------------+
| An example small FASTA file  | ``smbl.fasta.EXAMPLE_3``                                   |
+------------------------------+------------------------------------------------------------+
| Human genome HG38 (GRCh38)   | ``smbl.fasta.HG38``, ``smbl.fasta.HUMAN_GRCH38``           |
+------------------------------+------------------------------------------------------------+

Example
~~~~~~~

The following example demonstrates how SMBL can be used for automatic installation of software.

Create an empty file named ``Snakefile`` with the following content:

.. code-block:: python

	import smbl
	include: smbl.include()

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
			# read simulation
			shell("{input[0]} -C 1 {input[2]} {params.PREF}")

			# creating BWA index of the reference sequence
			shell("{input[1]} index {input[2]}")

			# mapping by BWA
			shell("{input[1]} mem {input[2]} {params.PREF}.bfast.fastq > alignment.sam")


Run the script.

.. code-block:: bash

	snakemake


What happens:

1. An example FASTA file is downloaded
2. DwgSim and BWA are downloaded, compiled and installed
3. DwgSim simulates reads from the example Fasta file
4. These reads are mapped back to the reference by BWA (*alignment.sam* is created)
