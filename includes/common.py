#common.py
#THis file will keep all the common methods together that could
#be shared amongst units.

menu_indent = 5 #how many spaces from the left of the screen
menu_width = 60 # total width of menu

version  = "2.0"
Title = 'SHFT version ' + version  + ' by Jacques Coetzee'
ascii = [
' #####   ##   ##  #######  ######',
'##   ##  ##   ##  ##         ##  ',
'##       ##   ##  ##         ##  ',
' #####   #######  #####      ##  ',
'     ##  ##   ##  ##         ##  ',
'##   ##  ##   ##  ##         ##  ',
' #####   ##   ##  ##         ##  ',
'---------------------------------',
'   by Jacques Coetzee 2014       ',
'                                 '
]



def get_menu_header(descriptor):
	try:
		global menu_indent	
		global menu_width
		header = ''
		#Ascii art
		header += " "*menu_indent + "*"*menu_width + "\n"
			
		for line in ascii:
			width = len(line)
			start_indent = int((menu_width-width) /2) -1
			header += " "*menu_indent + "*" + " "*start_indent + line + " "*start_indent + " *" +	"\n" 

		header += " "*menu_indent + "*"*menu_width + "\n"
	
		#Menu Items

		header += "\n"
		header += " "*menu_indent +"Menu - %s\n" % descriptor
		header += " "*menu_indent +"=======%s\n" % ("="*len(descriptor))
		header += "\n"
		return header
	except Exception, e:
		print e
		raw_input('Error')

