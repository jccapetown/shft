#shodanhq.py
from includes.base_classes import Plugin_Base

class shodanhq(Plugin_Base):

	title = 'ShodanHq'
	description = "Opens ShodanHq landing page. "
	base_command = "iceweasel"
	ip_cidr = ''

	options = {}


	def __init__(self):

		#add Custom arguments
		self.options['Custom'] = {}
		self.options['Custom']['description'] = 'supply your own url to open'
		self.options['Custom']['value'] = 'http://www.shodanhq.com'
		self.options['Custom']['argument'] = 'custom'
		self.options['Custom']['index'] = 1
		self.options['Custom']['display'] = False

		





