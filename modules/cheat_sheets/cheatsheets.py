#shodanhq.py
from includes.base_classes import Plugin_Base

class cheatsheets(Plugin_Base):

	title = 'Cheat Sheets'
	description = "Shows known cheat sheets for applications on the internet"
	base_command = "iceweasel"

	choices = {}


	def __init__(self):

		self.choices['1'] = ['Metasploit', "http://www.cheatography.com/huntereight/cheat-sheets/metasploit-4-5-0-dev-15713"]

		





