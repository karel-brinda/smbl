from snakemake.utils import min_version
min_version("3.2")

include: "constants.py"

include: "fasta.snake.py"

## already included by fasta.snake.py
#include: "progs.snake.py"

rule __test_include_all__:
	input:
		[ALL_FAS, ALL_PROGS]

