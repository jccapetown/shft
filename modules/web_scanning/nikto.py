#zenhmap.py
from includes.base_classes import Plugin_Base

class nikto(Plugin_Base):

	title = 'Nikto'
	description = "Web application scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "nikto -C all"
	post_commands=[]

	options = {}
	
	def __init__(self):

		#add options for switch 
		self.options['switch1'] = {}
		self.options['switch1']['description'] = ''
		self.options['switch1']['value'] = '-host'
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

		#add options for switch 
		self.options['switch2'] = {}
		self.options['switch2']['description'] = ''
		self.options['switch2']['value'] = '-output'
		self.options['switch2']['argument'] = 'custom'
		self.options['switch2']['index'] = 3
		self.options['switch2']['display'] = False
		
		#add options for output 
		self.options['output'] = {}
		self.options['output']['description'] = 'result output file'
		self.options['output']['value'] = '/tmp/nikto.txt'
		self.options['output']['argument'] = 'custom'
		self.options['output']['index'] = 4
		self.options['output']['display'] = True


		#add options for switch 
		self.options['switch3'] = {}
		self.options['switch3']['description'] = ''
		self.options['switch3']['value'] = '-port'
		self.options['switch3']['argument'] = 'custom'
		self.options['switch3']['index'] = 5
		self.options['switch3']['display'] = False
		
		#add options for output 
		self.options['port'] = {}
		self.options['port']['description'] = 'web server port'
		self.options['port']['value'] = '80'
		self.options['port']['argument'] = 'custom'
		self.options['port']['index'] = 6
		self.options['port']['display'] = True



		


		





