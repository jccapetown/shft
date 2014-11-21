#base classes for abstraction

#Plugin Base class

class Plugin_Base(object):
	
	title = 'Your Plugin Name'
	description = "Your plugin description"
	noise_level = 'Active / Passive'
	pre_commands =[]
	base_command = "ls -l"
	post_commands=[]

	#Options will be used to set arguments for applications
	options = {}
	#Choices are used for multiple selection. 
	#If choices are present then no options will be parsed.
	#Choices are in the format [description, backendchoice]
	choices = {}

	#mark a file as standalone wich means the script will be executed as is.
	#if this is set then the run command in the class will be executed.
	#you can override the run command
	standalone = False

	enabled = True
	



