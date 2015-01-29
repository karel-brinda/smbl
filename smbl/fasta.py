import os
import smbl

EXAMPLE                             = os.path.join(smbl.fa_dir,"example_fasta.fa")
HUMAN_HG38 = HUMAN_GRCH38           = os.path.join(smbl.fa_dir,"hg38.fa")

FAS = [
		EXAMPLE,
		HUMAN_HG38
	]

FAIS = ["{}.fai".format(fa) for fa in FAS]

ALL = FAS + FAIS
