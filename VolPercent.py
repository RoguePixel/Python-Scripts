#!/usr/bin/env python
from sys import argv as arg
import os

##255 is 100% PCM Volume

#function that also calculates percentage of volume
def percentvol(value):
	vol=int(value)*255/100	
	cmd="""amixer set 'PCM' """
	os.system(cmd + ' ' + str(vol))

def percent(value):
	vol=int(value)*255/100	
	yield vol

def volume(value):
	cmd="""amixer set 'PCM' """
	os.system(cmd + ' ' + str(value))
	

#for some reason cannot emulate same outcome of expression in the "raw_input" conjuctures. Had to create seperate function with ability to calc percentage.

if len(arg)>1:
	print
	percentvol(arg[1])
	print("  \n set volume:  %s%% \n") % (arg[1])
	
	
else:
	rinput=raw_input("\nEnter volume level (1-100):\n")
	for val in percent(rinput):
		print
		volume(val)
 		print("  \n set volume:  %s%% \n") % (rinput)
	
