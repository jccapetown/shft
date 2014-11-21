import os

class report():

	name = ''
	path = '' 

	def __init__(self, reportname, path):
		self.name = reportname
		self.path = path + "/reports/"
		self.initialise()


	def initialise(self):
		print self.path + self.name
		if os.path.exists(self.path + self.name):
			print "Found"
		else:
			os.system('mkdir %s' % self.path + self.name)		
			

