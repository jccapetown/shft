#zenhmap.py
from includes.base_classes import Plugin_Base

class webscarab(Plugin_Base):

	title = 'Webscarab'
	description = "Web application scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "webscarab"
	post_commands=[]

	options = {}
	
