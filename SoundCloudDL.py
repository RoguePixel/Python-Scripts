#!/usr/bin/env python
#SoundCloud Downloader

from sys import argv as arg
from subprocess import call
import os
import urllib
import fnmatch
import string
#import re
#"http://soundcloud.com/search?q%5Bfulltext%5D=king+singers"

if len(arg)==1:
	print "\n%s requires url \n" % arg[0]
	raise SystemExit
	
url=urllib.urlopen("%s") % arg[1]
html=url.read()
ulist=list(i for i in html.split(":"))
titlelist=[]
urllist=[]



# get titles of songs
for i in ulist:
	if fnmatch.fnmatch(i, "*streamUrl*"):
		title=i.replace('-',' ').replace('/',' ').split()
		titleformatted=string.capwords(' '.join(title[1:-2]))
		#print "%s" % titleformatted
		#add title to list
		titlelist.append(titleformatted)


#get url path of song
for i in ulist:
	if fnmatch.fnmatch(i, "*//media*"): #append "http:" to search results
		url=i.split(',')[0]
		#print "http:"+url
		urllist.append("\"http:"+url)


for i in range(0,len(urllist)):
	fname=urllist[i]
	cmd="\n wget -cnd %s -O \"%s\".mp3" % (urllist[i],titlelist[i])
	print cmd
	os.system(cmd)
	
# n=0
# for i in urllist:
# 	n+=1
# 	print "%s: %s" % (n,i)


