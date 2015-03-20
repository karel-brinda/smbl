import pytest
import smbl

@pytest.mark.parametrize("plugin,plugin_name", 
		[
			(x,x.get_plugin_name())
			for x in smbl.prog.plugins.get_registered_plugins() if x.is_platform_supported()
		]
	)
def test_plugins(plugin,plugin_name):
	plugin.install_all_steps()
	assert 1==1