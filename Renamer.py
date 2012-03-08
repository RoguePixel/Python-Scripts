#!/usr/bin/env python
from sys import argv as arg
import os, os.path

def renamer(path=os.getcwd(),keyword=None):
	for file in os.listdir(path):
		ext=os.path.splitext(file)
		for af in ('.mp3','.aac','.flac','.m4a'):
			if ext[1]==af:
				yield file,ext,os.path.join(path,file)

songlist=list(song for song in renamer(arg[1]))



# for i in songlist:
# 	print (i[1])[1]
try:
	for i in songlist:
		# print "rename?:\t %s" % (i[0])
		fname=raw_input("\nrename? (enter to skip):\n\n\t %s \n\nNew name:\t" % (i[0]))
		if not fname:
			print "\n %s not renamed" % (i[0])
		elif os.path.isfile(os.path.join(arg[1],fname+(i[1])[1])):
			print "file %s already exists" % fname
			fname2=raw_input("\nfile %s already exists! \nrename? (enter to skip):\n\n\t %s \n\nNew name:\t" % ((i[0]),fname))
			if not fname2:
				pass
		else:
			print "%s \n %s" % (i[2],os.path.join(os.path.abspath(arg[1]),fname)+(i[1])[1]) #os.rename(i[2],fname+(i[1])[1])
			os.rename(i[2],os.path.join(os.path.abspath(arg[1]),fname)+(i[1])[1])
			
except KeyboardInterrupt:
	print "\n\nexiting script..."