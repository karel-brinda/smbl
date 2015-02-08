import os
import smbl

EXAMPLE_1 = EXAMPLE                 = os.path.join(smbl.fa_dir,"example_fasta_1.fa")
EXAMPLE_2                           = os.path.join(smbl.fa_dir,"example_fasta_2.fa")
EXAMPLE_3                           = os.path.join(smbl.fa_dir,"example_fasta_3.fa")



HUMAN_HG38 = HUMAN_GRCH38           = os.path.join(smbl.fa_dir,"hg38.fa")

FAS = [
		EXAMPLE_1,
		EXAMPLE_2,
		EXAMPLE_3,
		HUMAN_HG38
	]

FAIS = ["{}.fai".format(fa) for fa in FAS]

ALL = FAS + FAIS
