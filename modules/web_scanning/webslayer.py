#zenhmap.py
from includes.base_classes import Plugin_Base

class webslayer(Plugin_Base):

	title = 'Webslayer'
	description = "Web application scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "webslayer"
	post_commands=[]

	options = {}
	
