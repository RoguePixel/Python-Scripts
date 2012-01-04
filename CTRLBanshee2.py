#!/usr/bin/env python

##ControlBanshee.py:
##python hack script to control playback of the banshee media player by executing tty commands
##
 
import os

##list of commands (can be reused for any applications)
bcoms={ 'p':'banshee --toggle-playing',
	'n':'banshee --next',
	'b':'banshee --previous',
	's':'banshee --stop'
}

print '\n'

for key in bcoms:
		print key,':',  bcoms[key]


		
while True:
	try:
		arg=raw_input("\nCommand:\n")
		
	
		for key in bcoms:
			print key,':',  bcoms[key]

		print '\n',  bcoms[arg] 		
		os.system(bcoms[arg])
	
		
	except: 
		if len(arg)!=0:
			print '\nno command associated with', arg
		else:
			print "no input. exiting...\n"
			break




