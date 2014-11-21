#!/usr/bin/python
#reporting.py

#This file will help generate output files for reporting purposes on work done.
#It will be the main class for generating the reports.

#every report will receive a name from the user. It will then generate a folder in the rports folder for this report and create layouts for the reports in html.

import os
from includes import classes
from includes import base_classes

class reporting(Plugin_Base):
#**********************************
#MAIN FUNCTION

	standalone = True

	def run(self):
		os.system('clear')
		#get a report name from the user
		print "SHFT report builder"
		print ""
		path= os.path.dirname(os.path.abspath(__file__))
		reportname = ''
		while reportname.strip() == '':
			reportname = raw_input("Please enter a report name: ")


		report = classes.report(reportname, path)










