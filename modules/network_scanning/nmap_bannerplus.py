#nmap_banner_plus
from includes.base_classes import Plugin_Base

class nmap_bannerplus(Plugin_Base):

	title = 'Nmap - banner plus'
	noise_level = 'Active'	
	description = "Performs fast scans via the banner-plus nse module"
	base_command = "nmap"

	options = {}

	def __init__(self):

		#add ip or cidr range
		self.options['ip'] = {}
		self.options['ip']['description'] = 'Normal nmap Ip or cidr range'
		self.options['ip']['value'] = ''
		self.options['ip']['argument'] = 'custom'
		self.options['ip']['index'] = 1
		self.options['ip']['display'] = True
		
		#add Custom arguments
		self.options['Custom'] = {}
		self.options['Custom']['description'] = 'supply your own arguments'
		self.options['Custom']['value'] = '--script /usr/share/nmap/scripts/banner-plus.nse --min-rate=400 --min-parallelism=64 -p1-65535 -n -Pn -PS -oA /tmp/report'
		self.options['Custom']['argument'] = 'custom'
		self.options['Custom']['index'] = 2
		self.options['Custom']['display'] = True

		





