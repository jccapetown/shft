#zenhmap.py
from includes.base_classes import Plugin_Base

class ping(Plugin_Base):

	title = 'Ping'
	description = "Ping a host on the network"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "ping"
	post_commands=[]

	options = {}


	def __init__(self):
		#add ip
		self.options['ip'] = {}
		self.options['ip']['description'] = 'Host ip to ping'
		self.options['ip']['value'] = ''
		self.options['ip']['argument'] = 'custom'
		self.options['ip']['index'] = 2
		self.options['ip']['display'] = True
		
		#add custom arguments
		self.options['arg'] = {}
		self.options['arg']['description'] = 'custom pping arguments'
		self.options['arg']['value'] = ''
		self.options['arg']['argument'] = 'custom'
		self.options['arg']['index'] = 1
		self.options['arg']['display'] = True



		





