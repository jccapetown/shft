#nslookup.py
from includes.base_classes import Plugin_Base

class fierce(Plugin_Base):

	title = 'fierce'
	description = "DNS Scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "fierce -dns"
	post_commands=[]

	options = {}

	def __init__(self):

		#add ip or cidr range
		self.options['domain'] = {}
		self.options['domain']['description'] = 'Custom options'
		self.options['domain']['value'] = ''
		self.options['domain']['argument'] = 'custom'
		self.options['domain']['index'] = 1
		self.options['domain']['display'] = True


		





