#discover.py
from includes.base_classes import Plugin_Base

class discover(Plugin_Base):

	title = 'Discover Scripts - Lee Baird'
	description = "Passive footprinting tool for discovery of targets"
	noise_level = 'Passive'
	pre_commands =['cd /opt/discover']
	base_command = "./discover.sh"
	post_commands=[]

	options = {}



		





