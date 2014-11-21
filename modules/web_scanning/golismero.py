#zenhmap.py
from includes.base_classes import Plugin_Base

class golismero(Plugin_Base):

	title = 'Golismero'
	description = "Web application scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "golismero"
	post_commands=[]

	options = {}
	
	def __init__(self):

		#add options for OS banner grabbing
		self.options['OS'] = {}
		self.options['OS']['description'] = 'attempt to identify the OS'
		self.options['OS']['value'] = 'scan'
		self.options['OS']['argument'] = 'custom'
		self.options['OS']['index'] = 1
		self.options['OS']['display'] = False

		#add host arguments
		self.options['host'] = {}
		self.options['host']['description'] = 'web host to scan'
		self.options['host']['value'] = ''
		self.options['host']['argument'] = 'custom'
		self.options['host']['index'] = 2
		self.options['host']['display'] = True

		



		





