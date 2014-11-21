#plugin.py

#this file will be responsible for deploying our plugins and making them work.

import importlib	#used to dynamically import classes from random scripts
import os, datetime
import common

class plugin():
	#Globals assignment for the class
	plugin_info = None
	application_path = None
	module = None
	plugin_class_pointer = None
	plugin_class = None
	option_list = []
	
	def __init__(self, plugin_info, application_path):
		self.plugin_info = plugin_info
		self.application_path = application_path

	
	def can_initialise(self):
		#we need to make sure that the plugin can be loaded with some
		#response to the user if it fails.
		try:

			#print self.plugin_info
			#create string reference to the module from the path
			#this wil be in the format "folder.folder.pyfile
			import_plugin = self.plugin_info['dir'].replace("/", ".") + '.' + self.plugin_info['module']
			self.module = importlib.import_module(import_plugin)
			#now load the class pointer inside the py file
			self.plugin_class_pointer = getattr(self.module, self.plugin_info['module'])
			#now create an instance of the class inside the module
			self.plugin_class = self.plugin_class_pointer()
			

			#check if the plugin is enabled
			if not self.plugin_class.enabled:
				return False

			# check if there are choices or if there are options
			if len(self.plugin_class.choices) == 0:
				self.load_options()

			return True
		except Exception, e:
			print e
			raw_input("Error: " )
			return False


	def load_options(self):
		self.option_list = []
		try:
			#Lets sort the arguments first
			tmplist = []
			for option in self.plugin_class.options:
				tmplist.append(self.plugin_class.options[option]['index'])
			
			tmplist = sorted(tmplist)
			for ix in tmplist:
				for option in self.plugin_class.options:
					if self.plugin_class.options[option]['index'] == ix:
						self.option_list.append(option)
		except Exception, e:
				print e
				self.option_list = []	
				for option in self.plugin_class.options:
					self.option_list.append(option)



	

	def run(self):
		if self.plugin_class.standalone:
			self.plugin_class.run()
			return
		
		if len(self.plugin_class.choices) > 0:
			self.run_choices()
			return

		command = ''
		while command.lower() != 'x':
			errormsg = ''	
			#Check for Command Input:
			command = command.strip()

			if command.lower() == 'r':
				#Execute the app here			
				self.run_plugin()
						
			
			elif command.lower() == 'h':
				self.show_help()

			elif '=' in command:
				command_lst = command.split('=')
				command = command_lst[0].strip()
				command_value = command_lst[1].strip()
				
				#see if we are altering option values
				for option in self.option_list:
					if command.lower() == option.lower():
						self.plugin_class.options[option]['value'] = command_value
				
			else:
				if command!='':
					errormsg = "Unknown Command -> %s" % command
								
			
			#create the screen
			os.system('clear')
			print common.get_menu_header(self.plugin_class.title)
			#displayscreen = "\n%s" % (self.plugin_class.title)
			displayscreen = ""
			
			#noise level	
			displayscreen += " "*common.menu_indent + "Noise Level: %s" % (self.plugin_class.noise_level) + "\n"
			
			#get the description of the tool
			displayscreen += " "*common.menu_indent + "Description: %s" % (self.plugin_class.description) + "\n"
			#displayscreen += "\n%s" % ("="*len(self.plugin_class.description))
			
			#get the options
			if len(self.plugin_class.options) > 0:
				displayscreen += " "*common.menu_indent + "%s\n" % "Option         Value                          Description"
				displayscreen += " "*common.menu_indent + "%s\n" % "======         =====                          ==========="
			
			try:
				for option in self.plugin_class.options:
					if 'display' in self.plugin_class.options[option]:
						if self.plugin_class.options[option]['display'] == False:
							continue
					record = option[0:13].ljust(15) + \
									 str(self.plugin_class.options[option]['value'])[0:29].ljust(31) + \
									 str(self.plugin_class.options[option]['description'][0:25].ljust(25))  
										
					displayscreen += " "*common.menu_indent + "%s\n" % (record)
					
				print displayscreen
				print ""
				print " "*common.menu_indent + "x. exit"
				print " "*common.menu_indent + "h. help"
				print " "*common.menu_indent + "r. run plugin"
				now = datetime.datetime.now()
				if errormsg != '':
					print " "*common.menu_indent + str(now) + ' : ' +  errormsg
				else:
					print ""
				print ""
			
				command = raw_input("~ SHFT "+ common.version +": > ")

			except Exception, e:
				print e
				raw_input("Error")
		#always go back to the current working dir
		os.chdir(application_path)
	

	

	def run_plugin(self):
		try:
			command = ''
			#first execute any pre commands
			for cmd in self.plugin_class.pre_commands:
				command += cmd + "; "
			
			#Lets sort the arguments first
			tmplist = []
			for option in self.plugin_class.options:
				tmplist.append(self.plugin_class.options[option]['index'])
			
			#Execute the plugin
			command += self.plugin_class.base_command 
			
			tmplist = sorted(tmplist)
			for ix in tmplist:
				#check if the argument is in the list, find it, and get the arguments in order
				for option in self.plugin_class.options:
					if self.plugin_class.options[option]['index'] == ix:
						#Get the command
						if self.plugin_class.options[option]['argument'].lower() == 'custom':
							command += " " + self.plugin_class.options[option]['value']
						elif str(self.plugin_class.options[option]['value']).lower() == 'true':
							command += " " + self.plugin_class.options[option]['argument']
	
			#print self.option_list
			#print 'gnome-terminal -t "SHFT 2.0 - Jacques Coetzee" --working-directory=WORK_DIR -x bash -c "%s; bash" ' % command
			#raw_input("The command above wil be executed")
			execstr = 'gnome-terminal -t "SHFT 2.0 - Jacques Coetzee" --working-directory=WORK_DIR -x bash -c "%s; bash" ' % command
			os.system(execstr)
		except Exception, e:
			print e.message
			raw_input("An Error Has Occured...")
			pass



	def show_help(self):
		try:
			command = ''
			#first execute any pre commands
			for cmd in self.plugin_class.pre_commands:
				command += cmd + "; "
			#Execute the plugin
			command += self.plugin_class.base_command + ' --help'

			execstr = 'gnome-terminal -t "SHFT 2.0 - Jacques Coetzee" --working-directory=WORK_DIR -x bash -c "%s; bash" ' % command
			os.system(execstr)
		except Exception, e:
			print e.message
			raw_input("test")




	def run_choices(self):
		try:
			command = ''
			while command != 'x':	

				for index in self.plugin_class.choices:
					if command == index:
						cmd = self.plugin_class.base_command + " "
						cmd += self.plugin_class.choices[index][1]
						#raw_input(cmd)
						execstr = 'gnome-terminal -t "SHFT 2.0 - Jacques Coetzee" --working-directory=WORK_DIR -x bash -c "%s; bash" ' % cmd
						os.system(execstr)
						

				#create the screen
				os.system('clear')
				print common.get_menu_header(self.plugin_class.title)
				#displayscreen = "\n%s" % (self.plugin_class.title)
				displayscreen = ""
				
				#get the description of the tool
				displayscreen += " "*common.menu_indent + "Description: %s" % (self.plugin_class.description) + "\n"
				#displayscreen += "\n%s" % ("="*len(self.plugin_class.description))
				
				#get the options
				if len(self.plugin_class.choices) > 0:
					displayscreen += " "*common.menu_indent + "%s\n" % "Choice"
					displayscreen += " "*common.menu_indent + "%s\n" % "================"

					for index in self.plugin_class.choices:
						option = self.plugin_class.choices[index]
						record = str(index) + "." +	option[0][0:15].ljust(15) 
						displayscreen += " "*common.menu_indent + "%s\n" % (record)
					
					print displayscreen
					print ""
					print " "*common.menu_indent + "x. exit"
					print " "*common.menu_indent + "r. run choice"
					print " "
					
					command = raw_input("~ SHFT "+ common.version +": > ")
		except Exception, e:
			print e.message
			raw_input("Here")
			pass
				








	
