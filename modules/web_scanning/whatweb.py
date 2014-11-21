#zenhmap.py
from includes.base_classes import Plugin_Base

class whatweb(Plugin_Base):

	title = 'Whatweb'
	description = "Web application scanner"
	noise_level = 'Active - LOUD'
	pre_commands =[]
	base_command = "whatweb"
	post_commands=[]

	options = {}
	
	def __init__(self):

		#add options for switch 
		self.options['switch1'] = {}
		self.options['switch1']['description'] = ''
		self.options['switch1']['value'] = '-a 4'
		self.options['switch1']['argument'] = 'custom'
		self.options['switch1']['index'] = 1
		self.options['switch1']['display'] = False
	

		#add host arguments
		self.options['host'] = {}
		self.options['host']['description'] = 'web host to scan'
		self.options['host']['value'] = ''
		self.options['host']['argument'] = 'custom'
		self.options['host']['index'] = 2
		self.options['host']['display'] = True

