#zenhmap.py
from includes.base_classes import Plugin_Base

class zap(Plugin_Base):

	title = 'OWASP - Zed Application Proxy'
	description = "Web application scanner"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "owasp-zap"
	post_commands=[]

	options = {}
	
