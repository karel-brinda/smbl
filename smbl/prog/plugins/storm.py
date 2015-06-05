import smbl
import snakemake
import os

from ._program import *

from .cmake import *

STORM_NUCLEOTIDE = get_bin_file_path("storm-nucleotide")
STORM_COLOR      = get_bin_file_path("storm-color")


##########################################
##########################################


class Storm(Program):

	@classmethod
	def get_installation_files(cls):
		return [
				STORM_NUCLEOTIDE,
				STORM_COLOR,
			]

	@classmethod
	def depends_on(cls):
		return [
			CMake
		]

	@classmethod
	def install(cls):
		cls.svn_checkout("svn://scm.gforge.inria.fr/svnroot/storm/trunk","")
		if smbl.utils.is_osx():
			cls.run_cmake("")
		cls.run_make("")
		cls.install_file("storm-color",STORM_COLOR)
		cls.install_file("storm-nucleotide",STORM_NUCLEOTIDE)

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

		if fastq_2!=None:
			smbl.messages.error("Pair-end reads are not supported by SToRM",program="SMBL",subprogram="SToRM")
			raise NotImplementedError("SToRM supports only single-end reads.")

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
		
		smbl.utils.shell('"{storm}" -M 4 -A -g "{genome}" -r "{reads}" -N "{threads}" | "{samtools}" view -bS - > "{bam}"'.format(
				storm=STORM_NUCLEOTIDE,
				samtools=smbl.prog.SAMTOOLS,
				genome=self._fa_fn,
				reads=self._fq1_fn,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)

	def map_reads_input(self):
		return [
				STORM_NUCLEOTIDE,
				smbl.prog.SAMTOOLS,
				self._fa_fn,
				self._fq1_fn,
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]