#!/usr/bin/env python

from sys import argv as arg
import os, glob, fnmatch

#must type in quoted text: "*.ext"
#need to be able to input: .ext 
#Ex: script.py txt 
#then it would find all extensions matching the pattern

cwd=os.getcwd()


def findf(directory,pattern):
	listf=os.listdir(directory)
	for f in sorted(listf):
		if fnmatch.fnmatch(f,pattern):
			yield f


for files in findf(cwd,str(arg[1])):
	print files

