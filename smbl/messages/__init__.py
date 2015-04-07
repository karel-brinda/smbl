from termcolor import colored, cprint

def message(message,program=None,subprogram=None):

	if program==None:
		program_part=""
		subprogram_part=""
	else:
		program_part="[{}] ".format(program)
		if subprogram==None:
			subprogram_part=""
		else:
			subprogram_part="{}: ".format(subprogram)

	cprint(
		"".join([program_part,subprogram_part,message]),
		"blue",
		attrs=['bold'],
	)

def error(message,program=None,subprogram=None, exception=None):
	if exception!=None:
		assert issubclass(exception,Exception)

	if program==None:
		program_part=""
		subprogram_part=""
	else:
		program_part="[{}] ".format(program)
		if subprogram==None:
			subprogram_part=""
		else:
			subprogram_part="{}: ".format(subprogram)

	cprint(
		"".join([program_part,subprogram_part,"Error: ",message]),
		"red",
		attrs=['bold'],
	)

	if exception!=None:
		raise exception(message)
