class RnFormatter:
	def __init__(
				self,
				source=0,
				id_str_size=16,
				source_str_size=2,
				chr_str_size=2,
				pos_str_size=8,
			):
		self.source=source
		self.id_str_size=id_str_size
		self.source_str_size=source_str_size
		self.chr_str_size=chr_str_size
		self.pos_str_size=pos_str_size
	
	def process_read(self,read_id,read,prefix="",suffix=""):
		return read.stringize(
					id_str_size=self.id_str_size,
					source_str_size=self.source_str_size,
					chr_str_size=self.chr_str_size,
					pos_str_size=self.pos_str_size
				)


class Read:
	def __init__(self,
					blocks=[],
					read_id=0
				):
		self.read_id=read_id
		self.blocks=blocks

	def stringize(self,
					id_str_size,
					source_str_size,
					chr_str_size,
					pos_str_size
				):
		prefix = ""
		suffix = ""

		blocks_strings=[
				x.stringize(
					source_str_size=source_str_size,
					chr_str_size=chr_str_size,
					pos_str_size=pos_str_size
				) for x in self.blocks
			]

		read_name="___".join(
			[
				prefix,
				format(self.read_id,'x').zfill(id_str_size),
				",".join(blocks_strings),
				suffix
			]
		)

		return read_name


class Block:
	def __init__(self,
				source=0,
				chr=0,
				direction="N",
				left=0,
				right=0
			):
		self.source=int(source)
		self.chr=int(chr)
		self.direction=direction
		self.left=int(left)
		self.right=int(right)

	def stringize(self,
				source_str_size,
				chr_str_size,
				pos_str_size
			):
		return "({},{},{},{},{})".format(
				str(self.source).zfill(source_str_size),
				str(self.chr).zfill(chr_str_size),
				self.direction,
				str(self.left).zfill(pos_str_size),
				str(self.right).zfill(pos_str_size)
			)

