import smbl
import snakemake
import os

from ._program import *

BWA = os.path.join(smbl.bin_dir,"bwa")


##########################################
##########################################


class Bwa(Program):

	@classmethod
	def get_installation_files(cls):
		return [BWA]

	@classmethod
	def supported_platforms(cls):
		return ["cygwin","osx","linux"]

	@classmethod
	def install(cls):
		cls.git_clone("git://github.com/lh3/bwa","bwa")
		cls.run_make("bwa")
		cls.install_file("bwa/bwa",BWA)

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
			self._fa_fn+".amb",
			self._fa_fn+".ann",
			self._fa_fn+".bwt",
			self._fa_fn+".pac",
			self._fa_fn+".sa"
		]

	##########################################

	def make_index(self):
		smbl.utils.shell('"{bwa}" index {fa}'.format(
				bwa=BWA,
				fa=self._fa_fn,
			))

	def make_index_input(self):
		return [
				BWA,
				self._fa_fn,
			]

	def make_index_output(self):
		return [
				self.index_fns(),
			]

	##########################################

	def map_reads(self):
		smbl.messages.error("Subclass of class Bwa should be used",program="SMBL",subprogram="BWA")
		raise NotImplementedError("Subclass of class Bwa should be used")

	def map_reads_input(self):
		return [
				BWA,
				smbl.prog.SAMTOOLS,
				self.index_fns(),
				self._fa_fn,
				self.fq_fn(),
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]


##########################################
##########################################


class BwaMem(Bwa):
	def __init__(
				self,
				fasta,
				bam,
				fastq_1,
				fastq_2=None,
			):

		super().__init__(
					fasta=fasta,
					fastq_1=fastq_1,
					fastq_2=fastq_2,
					bam=bam,
				)

	def map_reads(self,number_of_threads=1):
		if self._fq2_fn==None:
			reads_string='"{}"'.format(self._fq1_fn)
		else:
			reads_string='"{}" "{}"'.format(self._fq1_fn,self._fq2_fn)

		smbl.utils.shell('"{bwa}" mem -t {threads} "{idx}" {reads_string} | "{samtools}" view -bS - > "{bam}"'.format(
				bwa=BWA,
				samtools=smbl.prog.SAMTOOLS,
				idx=self._fa_fn,
				reads_string=reads_string,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)


##########################################
##########################################


class BwaSw(Bwa):
	def __init__(
				self,
				fasta,
				bam,
				fastq_1,
				fastq_2=None,
			):

		super().__init__(
					fasta=fasta,
					fastq_1=fastq_1,
					fastq_2=fastq_2,
					bam=bam,
				)

	def map_reads(self,number_of_threads=1):
		if self._fq2_fn==None:
			reads_string='"{}"'.format(self._fq1_fn)
		else:
			reads_string='"{}" "{}"'.format(self._fq1_fn,self._fq2_fn)

		smbl.utils.shell('"{bwa}" bwasw -t {threads} "{idx}" {reads_string} | "{samtools}" view -bS - > "{bam}"'.format(
				bwa=BWA,
				samtools=smbl.prog.SAMTOOLS,
				idx=self._fa_fn,
				reads_string=reads_string,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)
