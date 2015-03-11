import smbl.prog
import random

all_platforms = ["linux","windows","macos","cygwin"]

class Program:
	def __init__(self):
		self.rules=[]
		smbl.prog.add_program_instance(self)

	@staticmethod
	def install(directory):
		pass

	@staticmethod
	def supported_platforms():
		pass

	def add_rule(self,rule):
		self.rules.append(rule)

class Rule:
	def __init__(self,input,output,run):
		self.input=input
		self.output=output
		self.run=run
