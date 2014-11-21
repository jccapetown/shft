#nmap.py
from includes.base_classes import Plugin_Base

class nmap(Plugin_Base):

	title = 'Nmap - Standard'
	description = "Enables NMAP scans via the SHFT framework"
	base_command = "nmap"
	ip_cidr = ''

	options = {}

	def __init__(self):

		#add ip or cidr range
		self.options['ip'] = {}
		self.options['ip']['description'] = 'Normal nmap Ip or cidr range'
		self.options['ip']['value'] = ''
		self.options['ip']['argument'] = 'custom'
		self.options['ip']['index'] = 1
		self.options['ip']['display'] = True
		
		#add options for stealth mode
		self.options['Stealth'] = {}
		self.options['Stealth']['description'] = 'Only does half-open scans'
		self.options['Stealth']['value'] = True
		self.options['Stealth']['argument'] = '-sS'
		self.options['Stealth']['index'] = 2
		self.options['Stealth']['display'] = True
		
		#add options for OS banner grabbing
		self.options['OS'] = {}
		self.options['OS']['description'] = 'attempt to identify the OS'
		self.options['OS']['value'] = False
		self.options['OS']['argument'] = '-O'
		self.options['OS']['index'] = 3
		self.options['OS']['display'] = True

		#add Custom arguments
		self.options['Custom'] = {}
		self.options['Custom']['description'] = 'supply your own arguments like -sS -p1-23 etc'
		self.options['Custom']['value'] = ''
		self.options['Custom']['argument'] = 'custom'
		self.options['Custom']['index'] = 4
		self.options['Custom']['display'] = True

		





