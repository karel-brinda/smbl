import smbl
import snakemake
import os

__FASTAFILES = set()

def register_fasta(fastafile):
	__FASTAFILES.add(fastafile)

def get_registered_fastas():
	return list(__FASTAFILES)

def get_fa_file_path(fasta):
	return os.path.join(smbl.fa_dir,fasta)

def fasta_file(name,address):
	return FastaFile(name=name,address=address).get()


class FastaFile:
	verbosity=False

	def __init__(self,name,address):
		self.name=name
		self.filename_short=get_fa_file_path("{}.fa".format(name))
		self.filename_full=os.path.abspath(self.filename_short)
		self.address=address
		self.src_dir=os.path.join(smbl.src_dir,self.name)

		if self.address[-3:]==".gz":
			self.format="gz"
		elif self.address[-5:]==".2bit":
			self.format="2bit"
		else:
			self.format="fa"

		register_fasta(self)
		
	def get(self):
		return self.filename_full

	def get_required_programs(self):
		if self.format=="2bit":
			return [smbl.prog.TWOBITTOFA]
		else:
			return []

	def install_all_steps(self):
		self.status_message("Installation started")
		self.install_pre()
		self.install()
		self.install_post()
		self.status_message("Installation completed")

	def install_pre(self):
		self.shell('rm -fR "{src_dir}"'.format(src_dir=self.src_dir))
		self.shell('mkdir -p "{src_dir}"'.format(src_dir=self.src_dir))

	def install(self):
		if self.format=="gz":
			archive=self.download(
				filename_full=self.abs_from_short("{}.gz".format(self.name))
			)
			self.extract_gz(
				filename_full_archive=archive,
				filename_full_file=self.filename_full,
			)
		elif self.format=="2bit":
			archive=self.download(
				filename_full=self.abs_from_short("{}.2bit".format(self.name))
			)
			self.extract_2bit(
				filename_full_archive=archive,
				filename_full_file=self.filename_full,
			)
		elif self.format=="fa":
			self.download(
				filename_full=self.filename_full
			)
		else:
			em="Unknown format '{}'".format(self.format)
			smbl.messages.error(em,program="SMBL")
			raise NotImplementedError(em)

	def install_post(self):
		self.shell('rm -fR "{src_dir}"'.format(src_dir=self.src_dir))

	def download(self,filename_full):
		self.status_message("Downloading a file: "+self.address)
		self.shell('mkdir -p "{dir}"'.format(dir=os.path.dirname(filename_full)))
		try:
			self.shell('curl -L --insecure -o "{fn}" "{address}"'.format(
					fn=filename_full,
					address=self.address,
				))
		except:
			self.shell('curl -L --insecure -o "{fn}" "{address}"'.format(
					fn=filename_full,
					address=self.address
				))
		return filename_full

	def extract_gz(self,filename_full_archive,filename_full_file):
		self.status_message("Extracting an archive: {}".format(filename_full_archive))
		self.shell('gzip -d "{}" -c > "{}"'.format(
				filename_full_archive,
				filename_full_file
			))

	def extract_2bit(self,filename_full_archive,filename_full_file):
		self.status_message("Extracting a 2bit file: {}".format(filename_full_archive))
		self.shell('"{}" "{}" "{}"'.format(
				smbl.prog.TWOBITTOFA,
				filename_full_archive,
				filename_full_file
			))

	def install_file(self,filename_short,dest):
		self.status_message("Moving: "+self.abs_from_short(filename_short))
		filename_full=self.abs_from_short(filename_short)
		self.shell('mv "{source}" "{dest}"'.format(source=filename_full,dest=dest))
		if executable:
			self.shell('chmod +x "{}"'.format(dest))

	def shell(self,command):
		if self.verbosity:
			smbl.utils.shell(command)
		else:
			smbl.utils.shell("({}) > /dev/null".format(command))

	def status_message(self,message):
		smbl.messages.message(
			message=message,
			program="SMBL",
			subprogram=self.name,
		)

	def abs_from_short(self,short):
		return os.path.abspath(os.path.join(self.src_dir,short))

	@classmethod
	def set_verbosity(cls,verbosity):
		cls.verbosity=verbosity		

