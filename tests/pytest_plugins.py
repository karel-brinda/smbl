import pytest
import smbl

# todo: ensure that cmake is installed

smbl.prog.CMake.install_all_steps()

@pytest.mark.parametrize("plugin,plugin_name", 
		[
			(x,x.get_plugin_name())
			for x in smbl.prog.plugins.get_registered_plugins() if x.is_platform_supported() and x is not smbl.prog.CMake
		]
	)
def test_plugins(plugin,plugin_name):
	plugin.install_all_steps()
	assert 1==1
