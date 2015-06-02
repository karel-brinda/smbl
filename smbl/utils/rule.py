import smbl

__RULES=set()

def register_rule(rule):
	registered_rules=[r.encode() for r in get_registered_rules()]

	if rule.encode() not in registered_rules:
		__RULES.add(rule)

def get_registered_rules():
	return list(__RULES)

class Rule:
	def __init__(self,input,output,run):
		self.__input=input
		self.__output=output
		self.__run=run

		register_rule(self)

	def get_input(self):
		return self.__input

	def get_output(self):
		return self.__output

	def run(self):
		self.__run()

	def encode(self):
		return "{} {}".format(str(self.__input),str(self.__output))
