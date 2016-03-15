#!/usr/bin/env python

import sys, os, errno
from subprocess import Popen, PIPE

old_hmmdefs = open('hmmdefs','r')
new_hmmdefs = open('hmmdefs-updated','w')

kwargs = {'stdin': PIPE, 'stdout':PIPE, 'stderr':PIPE}

with open('hmmdefs','r') as hmmdefs_old:
	for monophone in hmmdefs_old:
		with open("proto-hmmdefs","r") as proto_hmmdefs:
			new_hmmdefs.write("~h \"" + monophone.rstrip() + "\"\n")
			new_hmmdefs.write(proto_hmmdefs.read())
			print monophone

new_hmmdefs.write("\n")

old_hmmdefs.close()
new_hmmdefs.close()


