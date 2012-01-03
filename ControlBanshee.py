#!/usr/bin/env python

##ControlBanshee.py:
##python hack script to control playback of the banshee media player
##
 
import os
#from subprocess import call

menu="\ncommands: \n \
1: play/pause\n \
2: next\n \
3: previous\n \
4: pause\n \
5: stop\n \
q: exit \
"
print menu

def bansheecom(val):
		if val==("1"):
			return "banshee --toggle-playing"
		elif val==("2"):
			return "banshee --next"
		elif val==("3"):
			return "banshee --previous"
		elif val==("4"):
			return "banshee --pause"
		elif val==("5"):
			return "banshee --stop"
		elif int(val)>=6:
			return "no command available"
		else:
			return "banshee --show"
while True:

	arg=raw_input("\nCommand:\n")
	#print menu
	if len(arg)!=0:	
		if int(arg)<=5:
			print menu,"\n\n",bansheecom(arg)
			os.system(bansheecom(arg))
			#call(bansheecom(arg))
		else:
			print menu,"\n\nno command available!\n"
			#print "you typed", arg
			#print(len(arg))
	else:
		print "\nno input, exiting...\n"
		break
