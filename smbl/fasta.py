EXAMPLE           = "example_fasta.fa"
HG39              = "hg39.fa"

FAS = [
		EXAMPLE,
		#HG39
	]

FAIS = ["{}.fai".format(fa) for fa in FAS]

ALL = FAS + FAIS
