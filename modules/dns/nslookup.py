#nslookup.py
from includes.base_classes import Plugin_Base

class nslookup(Plugin_Base):

	title = 'nslookup'
	description = "DNS probing"
	noise_level = 'Active'
	pre_commands =[]
	base_command = "nslookup"
	post_commands=[]

	options = {}



		





