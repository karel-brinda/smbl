import smbl
import snakemake
import os

from ._program import *

BOWTIE2            = get_bin_file_path("bowtie2")
BOWTIE2_ALIGN_L    = get_bin_file_path("bowtie2-align-l")
BOWTIE2_ALIGN_S    = get_bin_file_path("bowtie2-align-s")
BOWTIE2_BUILD      = get_bin_file_path("bowtie2-build")
BOWTIE2_BUILD_L    = get_bin_file_path("bowtie2-build-l")
BOWTIE2_BUILD_S    = get_bin_file_path("bowtie2-build-s")
BOWTIE2_INSPECT    = get_bin_file_path("bowtie2-inspect")
BOWTIE2_INSPECT_L  = get_bin_file_path("bowtie2-inspect-l")
BOWTIE2_INSPECT_S  = get_bin_file_path("bowtie2-inspect-s")


##########################################
##########################################


class Bowtie2(Program):

	@classmethod
	def get_installation_files(cls):
		return [
				BOWTIE2,
				BOWTIE2_ALIGN_L,
				BOWTIE2_ALIGN_S,
				BOWTIE2_BUILD,
				BOWTIE2_BUILD_L,
				BOWTIE2_BUILD_S,
				BOWTIE2_INSPECT,
				BOWTIE2_INSPECT_L,
				BOWTIE2_INSPECT_S,
			]

	@classmethod
	def install(cls):
		gitdir_bcftools=cls.git_clone("git://github.com/BenLangmead/bowtie2","")
		cls.run_make("")
		cls.install_file("bowtie2",BOWTIE2)
		cls.install_file("bowtie2-align-l",BOWTIE2_ALIGN_L)
		cls.install_file("bowtie2-align-s",BOWTIE2_ALIGN_S)
		cls.install_file("bowtie2-build",BOWTIE2_BUILD)
		cls.install_file("bowtie2-build-l",BOWTIE2_BUILD_L)
		cls.install_file("bowtie2-build-s",BOWTIE2_BUILD_S)
		cls.install_file("bowtie2-inspect",BOWTIE2_INSPECT)
		cls.install_file("bowtie2-inspect-l",BOWTIE2_INSPECT_L)
		cls.install_file("bowtie2-inspect-s",BOWTIE2_INSPECT_S)

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]

	##########################################

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
			self._fa_fn+".1.bt2",
			self._fa_fn+".2.bt2",
			self._fa_fn+".3.bt2",
			self._fa_fn+".4.bt2",
			self._fa_fn+".rev.1.bt2",
			self._fa_fn+".rev.2.bt2",
		]

	##########################################

	def make_index(self):
		smbl.utils.shell('"{bt2b}" "{fa}" "{fa}"'.format(
				bt2b=BOWTIE2_BUILD,
				fa=self._fa_fn,
			))

	def make_index_input(self):
		return [
				BOWTIE2_BUILD,
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
			reads_string='-1 "{}" -2 "{}"'.format(self._fq1_fn,self._fq2_fn)

		smbl.utils.shell('"{bt2}" -p {threads} -x "{idx}" {reads_string} | "{samtools}" view -bS - > "{bam}"'.format(
				bt2=BOWTIE2,
				samtools=smbl.prog.SAMTOOLS,
				idx=self._fa_fn,
				reads_string=reads_string,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)

	def map_reads_input(self):
		return [
				BOWTIE2,
				smbl.prog.SAMTOOLS,
				self.index_fns(),
				self._fa_fn,
				self.fq_fn(),
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]
