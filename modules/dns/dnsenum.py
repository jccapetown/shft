#nslookup.py
from includes.base_classes import Plugin_Base

class dnschef(Plugin_Base):

	title = 'dnschef'
	description = "DNS Proxy"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "dnschef"
	post_commands=[]

	options = {}

	def __init__(self):

		#add ip or cidr range
		self.options['args'] = {}
		self.options['args']['description'] = 'Custom options'
		self.options['args']['value'] = ''
		self.options['args']['argument'] = 'custom'
		self.options['args']['index'] = 1
		self.options['args']['display'] = True


		





