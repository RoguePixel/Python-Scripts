#!/usr/bin env python
import sys

arg=sys.argv

#if not len(arg)<2:
#	print "\nrequired numerical input\n"

try:
	if int(arg[1]):
		print arg[1]," is a number"

except ValueError:
	print arg[0]," Requires numerical argument"
