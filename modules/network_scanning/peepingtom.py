#peepingtom
from includes.base_classes import Plugin_Base

class peepingtom(Plugin_Base):

	title = 'peepingtom - HTTP login finder'
	noise_level = 'Active'	
	description = "Scans a range of ip addresses for http logins and takes a screen shot of the login page and reconsiles all screens on one html page for investigation. The input file required is made from the name.gnmap file that is converted with the gnmap.pl tool (in the misc section)"
	base_command = "python peepingtom.py"
	pre_commands = ['cd /opt/peepingtom']
	options = {}

	def __init__(self):

		#add hidden arguments
		self.options['cmd'] = {}
		self.options['cmd']['description'] = 'required params'
		self.options['cmd']['value'] = '-b -l'
		self.options['cmd']['argument'] = 'custom'
		self.options['cmd']['index'] = 1
		self.options['cmd']['display'] = False

		#add Custom arguments
		self.options['iplist'] = {}
		self.options['iplist']['description'] = 'a File containing ips in the format ip:port. This file can be generated from the gnmap util in the misc folder from an Nmap .gnmap output file'
		self.options['iplist']['value'] = '/tmp/gnmap.ips.txt'
		self.options['iplist']['argument'] = 'custom'
		self.options['iplist']['index'] = 2
		self.options['iplist']['display'] = True


		





