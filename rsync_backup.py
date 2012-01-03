#!/usr/bin/python
import sys, os, subprocess

##
##RSYNC-BACKUP V1
#the script can be executed and by defualt the variables specified in the script will used, otherwise arguments may be passed to the script at runtime. This script can be used to sync remote files to a local directory or local files to a remote direcory specified at runtime.
##
##
#argument examples:
#":~$ rsync-backup.py -raz user@host:/some/dir/ /some/dir"
#":~$ rsync-backup.py user@host:/some/dir /local/dir
#":~$ rync-backup.py /some/local/dir/ user@host:/some/dir/"
##

call = os.system
arg = sys.argv

#when making external calls os.system executes commands without variable designation
#timestamp = call("echo $(date +%T_%F)")
#change the values of "ID" and opts to reflect your environment
ID = ("user", "some/local/direc/", "user@server:/some/remote/direc/")
opts = ("-ravui", "-e ssh", "-progress")
#sshopts =("")

print opts[0]

if len(arg) == 1: 
	#print "\nwill execute defualt command: \n" 
	rsync =('rsync ' + ' '+opts[0]+' '+opts[2]+' '+ ID[1] + ' ' +  ID[2])
	#print(rsync)	
	call(rsync
	
elif len(arg)<3:
	print "script requires at least three arguments"

else:
	
	if '-' in arg[1]:
		#print "using rsync flags"
		if '@' in arg[2]:
			#print "syncing from remote dir to local with flags"
			rsync = ('rsync'+' '+arg[1]+' '+arg[2]+' '+arg[3])
			#print(rsync)
			call(rsync)
		else:
			#print "syncing from local dir to remote with flags"
			rsync = ('rsync'+' '+arg[1]+' '+arg[2]+' '+arg[3])
			#print(rsync)
			call(rsync)

	elif '@' in arg[2]:
		#print "syncing from remote dir to local without flags"
		rsync = ('rsync'+' '+arg[1]+' '+arg[2])
		#print(rsync)		
		call(rsync)
	else:
		#print "syncing from local dir to remote with flags"
		rsync = ('rsync'+' '+arg[1]+' '+arg[2])
		#print(rsync)		
		call(rsync)
