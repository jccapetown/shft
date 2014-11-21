#shodanhq.py
from includes.base_classes import Plugin_Base

class gnmap(Plugin_Base):

	title = 'gnmap'
	noise_level = ''
	description = "Creates a clean list of IP's from an *.gnmap output file "
	pre_commands = ['cd /opt/peepingtom']
	base_command = " "
	options = {}


	def __init__(self):
		#add Custom arguments
		self.options['cmd'] = {}
		self.options['cmd']['description'] = ''
		self.options['cmd']['value'] = 'cat'
		self.options['cmd']['argument'] = 'custom'
		self.options['cmd']['index'] = 1
		self.options['cmd']['display'] = False
		

		#add Custom arguments
		self.options['gnmapfile'] = {}
		self.options['gnmapfile']['description'] = 'Set the location of the nmap outputfile'
		self.options['gnmapfile']['value'] = '/tmp/report.gnmap'
		self.options['gnmapfile']['argument'] = 'custom'
		self.options['gnmapfile']['index'] = 2
		self.options['gnmapfile']['display'] = True
		
		#add Custom arguments
		self.options['cmd2'] = {}
		self.options['cmd2']['value'] = '| perl ./gnmap.pl | grep http | cut -f 1,2 -d "," | tr "," ":" >'
		self.options['cmd2']['description'] = ''
		self.options['cmd2']['argument'] = 'custom'
		self.options['cmd2']['index'] = 3
		self.options['cmd2']['display'] = False
	
		#add output file
		self.options['output'] = {}
		self.options['output']['description'] = 'Set the location of the cleaned nmap file'
		self.options['output']['value'] = '/tmp/gnmap.ips.txt'
		self.options['output']['argument'] = 'custom'
		self.options['output']['display'] = True
		self.options['output']['index'] = 4





