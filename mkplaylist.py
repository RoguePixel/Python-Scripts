#!/usr/bin/env python
from sys import argv as arg
import glob, os, os.path, fnmatch

###TODO
#add control statements to take runtime multiple arguments
#add option to name playlist file (not needed)
#add function to find duplicate listings and or defunct file listing
###TODO


cwd=os.getcwd()
aformats=('*.mp3','*.aac','*.flac','*.wav','*.m4a')
playlist=open('playlist.m3u','a')
home=os.getenv('HOME')
fdir=' '.join(arg[1:])
#musicdir=' '.join(arg[1:])
#os.path.splitext(os.path.join(path,name))


def listaudiofiles(root=os.getcwd()):
	for path, dirs, files in os.walk(root):		
		for name in files:
			yield os.path.abspath(os.path.join(path,name))
################################################

if len(arg)==1:
	#fdir=cwd
	#print "print searching for audio in %s" % cwd
	print "specify directory"

playlistname=raw_input("\nname for playlist? (defualt is playlist)\n")

#choose to name resulting playlist file
if not playlistname:
	pass
else:
	playlist=open(playlistname+".m3u",'a')


for f in listaudiofiles(fdir):	
	ext=os.path.splitext(f)
	for format in aformats: 
		if "*"+ext[1]==format:
			f=str(f)
			#print f#, ext[1]
			playlist.write("%s\n" % f)

playlist.close




