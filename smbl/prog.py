import os
import smbl

ART_454            = os.path.join(smbl.bin_dir,"art_454")
ART_ILLUMINA       = os.path.join(smbl.bin_dir,"art_illumina")
ART_SOLID          = os.path.join(smbl.bin_dir,"art_solid")
BCFTOOLS           = os.path.join(smbl.bin_dir,"bcftools")
BFAST              = os.path.join(smbl.bin_dir,"bfast")
BGZIP              = os.path.join(smbl.bin_dir,"bgzip")
BWA                = os.path.join(smbl.bin_dir,"bwa")
DRFAST             = os.path.join(smbl.bin_dir,"drfast")
DWGSIM             = os.path.join(smbl.bin_dir,"dwgsim")
DWGSIM_EVAL        = os.path.join(smbl.bin_dir,"dwgsim_eval")
FREEC              = os.path.join(smbl.bin_dir,"freec")
GEM_INDEXER        = os.path.join(smbl.bin_dir,"gem-indexer")
GEM_MAPPER         = os.path.join(smbl.bin_dir,"gem-mapper")
GEM_2_SAM          = os.path.join(smbl.bin_dir,"gem-2-sam")
MASON              = os.path.join(smbl.bin_dir,"mason")
MRFAST             = os.path.join(smbl.bin_dir,"mrfast")
MRSFAST            = os.path.join(smbl.bin_dir,"mrsfast")
PERM               = os.path.join(smbl.bin_dir,"perm")
SAMTOOLS           = os.path.join(smbl.bin_dir,"samtools")
SIRFAST            = os.path.join(smbl.bin_dir,"sirfast")
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
		FREEC,
		GEM_INDEXER,
		GEM_MAPPER,
		GEM_2_SAM,
		MASON,
		PERM,
		SAMTOOLS,
		STORM_COLOR,
		STORM_NUCLEOTIDE,
		TABIX,
		TWOBITTOFA,
		WGSIM,
		WGSIM_EVAL,

		MRFAST,
		MRSFAST,
		DRFAST,
		SIRFAST,

	]
