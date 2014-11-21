#nslookup.py
from includes.base_classes import Plugin_Base

class darkstat(Plugin_Base):

	title = 'darkstat'
	description = "Network Traffic Monitor.Will sniff data packets and serve them on a web page"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "darkstat"
	post_commands=[]

	options = {}

	def __init__(self):

		#
		self.options['arg1'] = {}
		self.options['arg1']['description'] = 'Custom options'
		self.options['arg1']['value'] = '-i'
		self.options['arg1']['argument'] = 'custom'
		self.options['arg1']['index'] = 1
		self.options['arg1']['display'] = False

		self.options['interface'] = {}
		self.options['interface']['description'] = 'Custom options'
		self.options['interface']['value'] = 'eth0'
		self.options['interface']['argument'] = 'custom'
		self.options['interface']['index'] = 2
		self.options['interface']['display'] = True
		

		self.options['arg2'] = {}
		self.options['arg2']['description'] = 'port to serve webpage on'
		self.options['arg2']['value'] = '-p'
		self.options['arg2']['argument'] = 'custom'
		self.options['arg2']['index'] = 3
		self.options['arg2']['display'] = False


		self.options['port'] = {}
		self.options['port']['description'] = 'Port to serve webpages'
		self.options['port']['value'] = '80'
		self.options['port']['argument'] = 'custom'
		self.options['port']['index'] = 4
		self.options['port']['display'] = True

