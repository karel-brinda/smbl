import os
import smbl
#import smbl.prog.plugins

all_platforms = ["linux","windows","osx","cygwin"]

from .plugins import *

#
# create rules from plugins
#
for plugin in get_registered_plugins():
	smbl.utils.Rule(
		input=[
				p.get_installation_files() for p in plugin.depends_on()
			],
		output=plugin.get_installation_files(),
		run=plugin.install_all_steps,
	)



#from smbl.prog.plugins import *
#for i, plugin in enumerate(get_registered_plugins()):
#	rule:
#		output:
#			plugin.get_installation_files()
#		input:
#			[
#				p.get_installation_files() for p in plugin.depends_on()
#			]
#		params:
#			i=str(i),
#		run:
#			(smbl.prog.plugins.get_registered_plugins()[int(params.i)].install_all_steps)()