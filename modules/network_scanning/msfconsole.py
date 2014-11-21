#zenhmap.py
from includes.base_classes import Plugin_Base

class msfconsole(Plugin_Base):

	title = 'Msfconsole'
	description = "Scanning of targets for exploits"
	noise_level = 'Active'
	pre_commands =['service postgresql start']
	base_command = "msfconsole"
	post_commands=[]

	options = {}



		





