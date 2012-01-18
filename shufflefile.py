#!/usr/bin/env python
import os, random, sys

listdir=os.listdir(os.getcwd())

#iterate items into a dictionary
filedict={}
filelist=[]
shuffledfile=open('shuffled.m3u','w')

#propogate empty dictionary with list of files
for f in range(len(sorted(listdir))):
	filedict[f]=listdir[f]

#lists files in dir with corrosponding key value 
def filelistgen(dictionary):
	for key in dictionary:
		yield key,dictionary[key]
				
#reads from file and generates random order list
def shuffle(f):
	flines=[]	
	for line in f:
		flines.append(line)
	random.shuffle(flines)
	for line in flines:
		yield line


#print all files in current dir
for f in filelistgen(filedict):
	print f 		

#need try statement

fselect=raw_input("\nselect file to be printed:\n")
f=filedict[int(fselect)]
txtfile=open(f,"r")

#choose to name file
fname=raw_input("\nname file? (defualt is shuffled.m3u)\n")
if not fname:
	pass
else:
	shuffledfile=open(fname+'.m3u','w')
	
#generate list of file contents and add line to file
for i in shuffle(txtfile):
#don't print becuase of large files
#	sys.stdout.write(i)
	shuffledfile.write(i)

shuffledfile.close
		

