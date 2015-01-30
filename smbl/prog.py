import os
import smbl

ART_454            = os.path.join(smbl.bin_dir,"art_454")
ART_ILLUMINA       = os.path.join(smbl.bin_dir,"art_illumina")
ART_SOLID          = os.path.join(smbl.bin_dir,"art_solid")
BCFTOOLS           = os.path.join(smbl.bin_dir,"bcftools")
BFAST              = os.path.join(smbl.bin_dir,"bfast")
BGZIP              = os.path.join(smbl.bin_dir,"bgzip")
BWA                = os.path.join(smbl.bin_dir,"bwa")
DWGSIM             = os.path.join(smbl.bin_dir,"dwgsim")
DWGSIM_EVAL        = os.path.join(smbl.bin_dir,"dwgsim_eval")
GEM_INDEXER        = os.path.join(smbl.bin_dir,"gem-indexer")
GEM_MAPPER         = os.path.join(smbl.bin_dir,"gem-mapper")
GEM_2_SAM          = os.path.join(smbl.bin_dir,"gem-2-sam")
MASON              = os.path.join(smbl.bin_dir,"mason")
SAMTOOLS           = os.path.join(smbl.bin_dir,"samtools")
STORM_COLOR        = os.path.join(smbl.bin_dir,"storm-color")
STORM_NUCLEOTIDE   = os.path.join(smbl.bin_dir,"storm-nucleotide")
TABIX              = os.path.join(smbl.bin_dir,"tabix")
TWOBITTOFA         = os.path.join(smbl.bin_dir,"twoBitToFa")
WGSIM              = os.path.join(smbl.bin_dir,"wgsim")
WGSIM_EVAL         = os.path.join(smbl.bin_dir,"wgsim_eval.pl")

ALL = [
		ART_454,
		ART_ILLUMINA,
		ART_SOLID,
		BCFTOOLS,
		BFAST,
		BGZIP,
		BWA,
		DWGSIM,
		DWGSIM_EVAL,
		GEM_INDEXER,
		GEM_MAPPER,
		GEM_2_SAM,
		MASON,
		SAMTOOLS,
		STORM_COLOR,
		STORM_NUCLEOTIDE,
		TABIX,
		TWOBITTOFA,
		WGSIM,
		WGSIM_EVAL
	]
