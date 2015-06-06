import snakemake
import re


def shell(
			cmd,
			remove_spaces=True,
			async=False,
			iterable=False,
			read=False, 
		):
	if remove_spaces:
		#print("removing spaces from command")
		cmd=re.sub(r'[ \t\f\v]+',' ',cmd).strip()

	return snakemake.shell(
			cmd=cmd,
			async=async,
			iterable=iterable,
			read=read,
		)



