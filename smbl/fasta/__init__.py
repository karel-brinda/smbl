import os
import smbl

from .fastafile import *

EXAMPLE_1  = fasta_file("Mycobacterium_tuberculosis","ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Mycobacterium_tuberculosis_H37Rv_uid170532/NC_018143.fna")
EXAMPLE_2  = fasta_file("Chlamydia_trachomatis","ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Chlamydia_trachomatis_RC_L2_s_3_uid213390/NC_021897.fna")
EXAMPLE_3  = fasta_file("Borrelia_garinii","ftp://ftp.ncbi.nih.gov/genomes/Bacteria/Borrelia_garinii_BgVir_uid162165/NC_017717.fna")

EXAMPLE_42 = fasta_file("Human_chr_21","http://hgdownload.cse.ucsc.edu/goldenpath/hg19/chromosomes/chr21.fa.gz")

EXAMPLE = EXAMPLE_1

HUMAN_HG38 = fasta_file("hg38","http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/hg38.2bit")
MOUSE_MM10 = fasta_file("mm10","http://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/mm10.2bit")
CHIMP_PANTRO4 = fasta_file("panTro4","http://hgdownload.cse.ucsc.edu/goldenPath/panTro4/bigZips/panTro4.2bit")

for fasta in get_registered_fastas():
	smbl.utils.Rule(
		input=fasta.get_required_programs(),
		output=fasta.get(),
		run=fasta.install_all_steps,
	)
