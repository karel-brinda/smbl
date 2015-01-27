import os

bin_dir = os.path.join(os.path.expanduser("~"),".smbl","bin")
print("directory for programs: ",bin_dir)


ART_454         = os.path.join(bin_dir,"art_454")
ART_ILLUMINA    = os.path.join(bin_dir,"art_illumina")
ART_SOLID       = os.path.join(bin_dir,"art_solid")
BCFTOOLS        = os.path.join(bin_dir,"bcftools")
BGZIP           = os.path.join(bin_dir,"bgzip")
BWA             = os.path.join(bin_dir,"bwa")
DWGSIM          = os.path.join(bin_dir,"dwgsim")
DWGSIM_EVAL     = os.path.join(bin_dir,"dwgsim_eval")
SAMTOOLS        = os.path.join(bin_dir,"samtools")
TABIX           = os.path.join(bin_dir,"tabix")
WGSIM           = os.path.join(bin_dir,"wgsim")
WGSIM_EVAL      = os.path.join(bin_dir,"wgsim_eval.pl")

ALL = [
		DWGSIM,
		DWGSIM_EVAL,
		ART_454,
		ART_ILLUMINA,
		ART_SOLID,
		BCFTOOLS,
		BGZIP,
		BWA,
		SAMTOOLS,
		TABIX,
		WGSIM,
		WGSIM_EVAL
	]
