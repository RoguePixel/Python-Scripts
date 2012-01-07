#!/usr/bin/env python

from sys import argv as arg
import os

##300 is 100% PCM Volume
##implement conversion of 0-300 value to percentage then pass to external call.

def volume(value):
	cmd="""amixer set 'PCM' """
	os.system(cmd + ' ' + value)
	

if len(arg)>1:
	volume(arg[1])

else:
	rinput=raw_input("\nEnter volume level:\n")
	volume(rinput) 
	print "set volume: %s" % rinput 
	

