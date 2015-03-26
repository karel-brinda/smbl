import smbl
import snakemake
import os

import __program

GMAP_BUILD      = __program.get_bin_file_path("gmap_build")
GMAP            = __program.get_bin_file_path("gmapl")
GSNAP           = __program.get_bin_file_path("gsnapl")


##########################################
##########################################


class Gmap_Gsnap(__program.Program):

	version="2014-12-24"

	@classmethod
	def get_installation_files(cls):
		return [
				GMAP,
				GSNAP,
			]

	@classmethod
	def install(cls):
		fn=cls.download_file("http://research-pub.gene.com/gmap/src/gmap-gsnap-{ver}.tar.gz".format(ver=cls.version),"gmap-gsnap.tar.gz")
		dir=cls.extract_tar(fn,strip=1)
		cls.run_configure(dir)
		cls.run_make(dir)
#		cls.install_file("src/gmapindex",GMAP_INDEX)
		cls.install_file("src/gmapl",GMAP)
		cls.install_file("src/gsnapl",GSNAP)

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

#		smbl.prog.plugins.Rule(
#			input=self.make_index_input(),
#			output=self.make_index_output(),
#			run=self.make_index,
#		)

		smbl.prog.plugins.Rule(
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

#	def index_fns(self):
#		return [
#			self._fa_fn+".1.bt2",
#			self._fa_fn+".2.bt2",
#			self._fa_fn+".3.bt2",
#			self._fa_fn+".4.bt2",
#			self._fa_fn+".rev.1.bt2",
#			self._fa_fn+".rev.2.bt2",
#		]

	##########################################

	def map_reads(self,number_of_threads=1):
		if self._fq2_fn==None:
			reads_string='"{}"'.format(self._fq1_fn)
		else:
			reads_string='"{}" "{}"'.format(self._fq1_fn,self._fq2_fn)

		snakemake.shell('"{gsnap}" -A sam -d {idx} -t {threads} {reads_string} | "{samtools}" view -bS - > "{bam}"'.format(
				gsnap=GSNAP,
				samtools=smbl.prog.SAMTOOLS,
				idx=self._fa_fn,
				reads_string=reads_string,
				bam=self._bam_fn,
				threads=number_of_threads,
			)
		)

	def map_reads_input(self):
		return [
				GSNAP,
				smbl.prog.SAMTOOLS,
				#self.index_fns(),
				self._fa_fn,
				self.fq_fn(),
			]

	def map_reads_output(self):
		return [
				self.bam_fn(),
			]
