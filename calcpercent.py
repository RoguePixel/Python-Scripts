#!/usr/bin/ env python
from sys import argv as arg

#REFERENCE
#percent=num*100/300		
#25*300/100 = percentage
#75%/300*100 = value

#works! calculates percentage value
#print int(arg[1])*300/100	

def percentconverter(value):
	vol=int(value)*300/100	
	print vol
	
#value=raw_input("\nvolume level\n:")


#for i in percentconverter(arg[1]):
#	print i

percentconverter(arg[1])



