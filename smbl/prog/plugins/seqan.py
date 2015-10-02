import smbl
import snakemake
import os

from ._program import *

from .cmake import *
from .samtools import *

MASON_FRAG_SEQUENCING   = get_bin_file_path("mason_frag_sequencing")
MASON_GENOME            = get_bin_file_path("mason_genome")
MASON_MATERIALIZER      = get_bin_file_path("mason_materializer")
MASON_METHYLATION       = get_bin_file_path("mason_methylation")
MASON_SIMULATOR         = get_bin_file_path("mason_simulator")
MASON_SPLICING          = get_bin_file_path("mason_splicing")
MASON_VARIATOR          = get_bin_file_path("mason_variator")
YARA_INDEXER            = get_bin_file_path("yara_indexer")
YARA_MAPPER             = get_bin_file_path("yara_mapper")
#RAZERS1                 = get_bin_file_path("razers")
#RAZERS2                 = get_bin_file_path("razers2")
RAZERS3 = RAZER         = get_bin_file_path("razers3")


##########################################
##########################################


class Seqan(Program):

	@classmethod
	def get_installation_files(cls):
		return [
				MASON_FRAG_SEQUENCING,
				MASON_GENOME,
				MASON_MATERIALIZER,
				MASON_METHYLATION,
				MASON_SIMULATOR,
				MASON_SPLICING,
				MASON_VARIATOR,
				YARA_INDEXER,
				YARA_MAPPER,
#				RAZERS1,
#				RAZERS2,
				RAZERS3,
			]

	@classmethod
	def depends_on(cls):
		return [
			CMake,
			SamTools,
		]
		
	@classmethod
	def install(cls):

		cls.git_clone("git://github.com/seqan/seqan","")

		cls.run_cmake("")


		cls.run_make("apps/mason2")
		cls.install_file("bin/mason_frag_sequencing",MASON_FRAG_SEQUENCING)
		cls.install_file("bin/mason_genome",MASON_GENOME)
		cls.install_file("bin/mason_materializer",MASON_MATERIALIZER)
		cls.install_file("bin/mason_methylation",MASON_METHYLATION)
		cls.install_file("bin/mason_simulator",MASON_SIMULATOR)
		cls.install_file("bin/mason_splicing",MASON_SPLICING)
		cls.install_file("bin/mason_variator",MASON_VARIATOR)

#		cls.run_make("apps/razers")
#		cls.install_file("bin/razers",RAZERS1)
#
#		cls.run_make("apps/razers2")
#		cls.install_file("bin/razers2",RAZERS2)

		cls.run_make("apps/razers3")
		cls.install_file("bin/razers3",RAZERS3)

		cls.run_make("apps/yara")
		cls.install_file("bin/yara_indexer",YARA_INDEXER)
		cls.install_file("bin/yara_mapper",YARA_MAPPER)

	@classmethod
	def supported_platforms(cls):
		# cywgin has too old cmake
		return ["osx","linux"]


##########################################
##########################################


class RazerS3(Seqan):

	def __init__(
				self,
				fasta,
				bam,
				fastq_1,
				fastq_2=None,
			):

		super().__init__()


		self._fa_fn=fasta
		self._fq1_fn=fastq_1
		self._fq2_fn=fastq_2
		self._bam_fn=bam

		smbl.utils.Rule(
			input=self.map_reads_input(),
			output=self.map_reads_output(),
			run=self.map_reads,
		)

	def fq_fn(self):
		if self._fq2_fn==None:
			return [self._fq1_fn]
		else:
			return [self._fq1_fn,self._fq2_fn]

	def fa_fn(self):
		return self._fa_fn

	def bam_fn(self):
		return self._bam_fn

	##########################################

	def map_reads(self,number_of_threads=1):
		if self._fq2_fn==None:
			reads_string='"{}"'.format(self._fq1_fn)
		else:
			reads_string='"{}" "{}"'.format(self._fq1_fn,self._fq2_fn)

		smbl.utils.shell('("{razer}" -o "{bam}" -tc {threads} "{genome}" {reads_string}) > /dev/null'.format(
				razer=RAZERS3,
				genome=self._fa_fn,
				reads_string=reads_string,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)

	def map_reads_input(self):
		return [
				RAZERS3,
				self._fa_fn,
				self.fq_fn(),
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]


##########################################
##########################################


class Yara(Seqan):

	def __init__(
				self,
				fasta,
				bam,
				fastq_1,
				fastq_2=None,
				sort_by_name=False,
			):

		super().__init__()

		self._fa_fn=fasta
		self._fq1_fn=fastq_1
		self._fq2_fn=fastq_2
		self._bam_fn=bam
		self.index_prefix=self._fa_fn.rpartition(".")[0]
		self._sort_by_name=sort_by_name

		smbl.utils.Rule(
			input=self.make_index_input(),
			output=self.make_index_output(),
			run=self.make_index,
		)

		smbl.utils.Rule(
			input=self.map_reads_input(),
			output=self.map_reads_output(),
			run=self.map_reads,
		)

	def fq_fn(self):
		if self._fq2_fn==None:
			return [self._fq1_fn]
		else:
			return [self._fq1_fn,self._fq2_fn]

	def fa_fn(self):
		return self._fa_fn

	def bam_fn(self):
		return self._bam_fn

	def index_fns(self):
		return [
			self.index_prefix+".lf.drp",
			self.index_prefix+".lf.drs",
			self.index_prefix+".lf.drv",
			self.index_prefix+".lf.pst",
			self.index_prefix+".rid.concat",
			self.index_prefix+".rid.limits",
			self.index_prefix+".sa.ind",
			self.index_prefix+".sa.len",
			self.index_prefix+".sa.val",
			self.index_prefix+".txt.concat",
			self.index_prefix+".txt.limits",
			self.index_prefix+".txt.size",
		]

	##########################################

	def make_index(self):
		smbl.utils.shell('("{yara_indexer}" -o "{prefix}" "{fa}") > /dev/null'.format(
				yara_indexer=YARA_INDEXER,
				prefix=self.index_prefix,
				fa=self._fa_fn,
			))

	def make_index_input(self):
		return [
				YARA_INDEXER,
				self._fa_fn,
			]

	def make_index_output(self):
		return [
				self.index_fns(),
			]

	##########################################

	def map_reads(self,number_of_threads=1):
		if self._fq2_fn==None:
			reads_string='"{}"'.format(self._fq1_fn)
		else:
			reads_string='"{}" "{}"'.format(self._fq1_fn,self._fq2_fn)

		if self._sort_by_name:
			smbl.utils.shell('"{yara_mapper}" -t {threads} "{genome_pref}" {reads_string} | "{samtools}" sort -n - "{bamprefix}"'.format(
						yara_mapper=YARA_MAPPER,
						genome_pref=self.index_prefix,
						reads_string=reads_string,
						bamprefix=self._bam_fn[:-4],
						threads=number_of_threads,
						samtools=smbl.prog.SAMTOOLS,
					)
				)
		else:
			smbl.utils.shell('"{yara_mapper}" -o "{bam}" -t {threads} "{genome_pref}" {reads_string}'.format(
						yara_mapper=YARA_MAPPER,
						genome_pref=self.index_prefix,
						reads_string=reads_string,
						bam=self._bam_fn,
						threads=number_of_threads,
					)
				)

	def map_reads_input(self):
		return [
				YARA_MAPPER,
				self._fa_fn,
				self.fq_fn(),
				self.index_fns(),
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]
