#core.py


import glob,os
import plugin
import importlib
import common

#example to import string modules
#module = importlib.importmodule('nmap')
#myclass = getattr(module, 'nmap')
#nmap = myclass()
#nmap.somefunction()

class shftCore():

	#	Main Class that manages the Core of the system
	maindict = {}
	maindict['categories'] = {}
	application_path = os.path.dirname(os.path.abspath(__file__))	
	max_category_length = 0

	def __init__(self):
		#Constructor
		self.load_categories()

	
	def load_categories(self):
		#Loads all Category names
		dirs = os.listdir("modules")
		dirs.sort()
		ix = 0
		self.max_category_length = 0
		for catname in dirs:
			if os.path.isdir('modules/' + catname):				
				if not catname in self.maindict['categories']:
					ix+=1
					#get max category length for description placing on menus
					if len(catname) > self.max_category_length:
						self.max_category_length = len(catname)
					self.maindict['categories'][catname] = {} 
					self.maindict['categories'][catname]['location'] = '/modules/' 
					self.maindict['categories'][catname]['name'] = catname 
					self.maindict['categories'][catname]['index'] = ix
					self.maindict['categories'][catname]['tools'] = {}
					
					
					#Now let see if we can load those dynamic tools modules
					tools = []
					tool_ix = 0
					for dynamicclasspath in glob.glob('%s%s%s' % ('modules/', catname ,'/*.py') ):
						dir, file =  os.path.split(dynamicclasspath)	
						if "__init__.py" == file:
							continue
						#we need the tools sorted....
						tools.append(file)
					
					tools.sort()
					for tool in tools:
						tool_ix += 1
						dir = 'modules/' + catname 
						classname, extension = tool.split('.')				
						self.maindict['categories'][catname]['tools'][classname] = {}
						self.maindict['categories'][catname]['tools'][classname]['module'] = classname
						self.maindict['categories'][catname]['tools'][classname]['dir'] = dir
						self.maindict['categories'][catname]['tools'][classname]['path'] = dynamicclasspath
						self.maindict['categories'][catname]['tools'][classname]['ext'] = extension
						self.maindict['categories'][catname]['tools'][classname]['index'] = tool_ix

	
	def show_category_menu(self):
		selection = -1
		while selection != 'x':
			os.system('clear')
			menu = common.get_menu_header('Category')
			menu += "\n"
			categorycount = len(self.maindict['categories'])+1
			#order the menu items	
			for ix in range(1,categorycount):
				for category in self.maindict['categories']:
					if self.maindict['categories'][category]['index'] == ix:

						#create the menu item
						menu += " "*common.menu_indent + \
										str(self.maindict['categories'][category]['index']) + \
										". " + category.ljust(self.max_category_length + 3) + \
										"\n"


			menu +=  " "*common.menu_indent + "x. exit" + "\n"
			print menu
			#get user input
			selection = raw_input("Please make a selection: ")
			try:
				#see if a numeric was presented
				if int(selection) in range(1,categorycount):
					self.show_tools_menu(int(selection))
			except Exception, e:
				#print e
				#raw_input("Error Core")
				pass	



	def show_tools_menu(self, category_index):
		selection = ''
		while selection != 'x':	
			#get the category information
			os.system('clear')
			toolcount = 0
			for category in self.maindict['categories']:
				if self.maindict['categories'][category]['index'] == category_index:
					toolcount = len(self.maindict['categories'][category]['tools'])+1
					menu = common.get_menu_header(category + ' tools')
					#this is the category!
					#lets load the tools for it as a menu
					for ix in range(1, toolcount):
						for tool in self.maindict['categories'][category]['tools']:
							if self.maindict['categories'][category]['tools'][tool]['index'] == ix:
								menu += " "*common.menu_indent +  str(self.maindict['categories'][category]['tools'][tool]['index']) + ". " + tool + "\n"
			menu += " "*common.menu_indent + "x. exit" + "\n"
			print menu

			selection = raw_input("Please make a selection: ")
			try:
				#see if a numeric was presented
				if int(selection) in range(1,toolcount):
					self.load_plugin(category_index, int(selection))	
			except Exception, e:
				#print e.message
				pass


	def load_plugin(self, category_index, tool_index):
		#we need to find the plugin and then load it up!
		#search in all the categories
		for category in self.maindict['categories']:
			if self.maindict['categories'][category]['index'] == category_index:
				#for all their tools
				for tool in self.maindict['categories'][category]['tools']:
					if self.maindict['categories'][category]['tools'][tool]['index'] == tool_index: 
						#if we make it here we found the tool plugin!
						proc_plugin = plugin.plugin( self.maindict['categories'][category]['tools'][tool], self.application_path)
						if proc_plugin.can_initialise():
							proc_plugin.run()




