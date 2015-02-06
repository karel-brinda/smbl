#! /usr/bin/env python3

import re

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


read_destr_pattern = re.compile(r'(.*)__([0-9abcdef]+)__(\([0-9abcdefFRN,]*\))(,\([0-9abcdefFRN,]*\))*__(.*)')
class Read:
	def __init__(self,
					blocks=[],
					read_id=0
				):
		self.read_id=read_id
		self.blocks=blocks

	def stringize(self,
					id_str_size=1,
					source_str_size=1,
					chr_str_size=1,
					pos_str_size=1
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

		read_name="__".join(
			[
				prefix,
				format(self.read_id,'x').zfill(id_str_size),
				",".join(blocks_strings),
				suffix
			]
		)

		return read_name

	def destringize(self, text):
		#todo: assert -- starting with (, ending with )
		#(prefix,read_id,blocks_t,suffix)=(text).split("__")
		#blocks=blocks_t.split("),(")
		m=read_destr_pattern.match(text)
		groups=m.groups()
		#todo: check number of groups
		self.prefix=groups[0]
		read_id=groups[1]
		self.read_id=int(read_id,16)
		self.blocks=[]
		blocks_str=groups[2:-1]
		for b_str in blocks_str:
			if b_str is not None:
				if b_str[0]==",":
					b_str=b_str[1:]
				b=Block()
				b.destringize(b_str)
				self.blocks.append(b)
		self.suffix=groups[-1]

block_destr_pattern = re.compile(r'^\(([0-9]+),([0-9]+),([FRN]),([0-9]+),([0-9]+)\)$')
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
				source_str_size=1,
				chr_str_size=1,
				pos_str_size=1
			):
		pos_str_size=max(pos_str_size,len(str(self.left)),len(str(self.right)))
		return "({},{},{},{},{})".format(
				str(self.source).zfill(source_str_size),
				str(self.chr).zfill(chr_str_size),
				self.direction,
				str(self.left).zfill(pos_str_size),
				str(self.right).zfill(pos_str_size)
			)

	def destringize(self,string):
		print("block destr", string)
		m=block_destr_pattern.match(string)
		self.source=int(m.group(1))
		self.chr=int(m.group(2))
		self.direction=m.group(3)
		self.left=int(m.group(4))
		self.right=int(m.group(5))
		#TODO: checks:
		#   1. if reg match ok
		#   2. if variables ok left <= right, etc.


if __name__ == "__main__":
	print ("Test of the RNF module")

	print ()
	print ("1) BLOCK")
	print ()

	for block_repr in ["(0,0,N,0,0)","(0,1,F,56,59)","(0,1,R,01,59)"]:
		print("Original block string", block_repr)
		block=Block()
		block.destringize(block_repr)
		print("Block after destringization", block.stringize())

	print ()
	print ("2) READ")
	print ()


	read=Read()

	for read_name_test in [
				"__000324a__(2,3,R,34,3643),(4,3,F,1,56)__",
				"__00000000__(01,1,F,0390501,0000000)__"
			]:
		read.destringize(read_name_test)
		print()
		print("Original read string", read_name_test)
		print("Read after destringization", read.stringize ())
