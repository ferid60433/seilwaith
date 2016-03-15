#!/usr/bin/env python

import sys, os, errno
from subprocess import Popen, PIPE

old_hmmdefs = open('hmmdefs','r')
new_hmmdefs = open('hmmdefs-updated','w')

insil = False
insilcentrestate = False

parameters_list = []
gconst_list = []

def add_sp():
	newsp="""~h "sp"
<BEGINHMM>
<NUMSTATES> 3
<STATE> 2
<MEAN> 25
@@PARAMETER_0@@
<VARIANCE> 25
@@PARAMETER_1@@
@@GCONST_0@@
<TRANSP> 3
0.0 1.0 0.0
0.0 0.9 0.1
0.0 0.0 0.0
<ENDHMM>
"""
	for index, parameter_line in enumerate(parameters_list):
		replaceString = "@@PARAMETER_" + str(index) + "@@"
		newsp=newsp.replace(replaceString, parameter_line) 

	for index, gconst_line in enumerate(gconst_list):
		replaceString = "@@GCONST_" + str(index) + "@@"
		newsp=newsp.replace(replaceString, gconst_line)			

	new_hmmdefs.write(newsp)

	
with open('hmmdefs','r') as hmmdefs_old:

	for hmmdefs_line in hmmdefs_old:
		
		if '~h \"sil\"' in hmmdefs_line:
			insil=True
			new_hmmdefs.write(hmmdefs_line)
		elif insil is True:
			new_hmmdefs.write(hmmdefs_line)
			if '<ENDHMM>' in hmmdefs_line:
				add_sp()								
				insil=False
			else:
				if hmmdefs_line.startswith("<STATE> 3"):
					insilcentrestate=True
				
				if insilcentrestate and "<GCONST>" in hmmdefs_line:
					gconst_list.append(hmmdefs_line.rstrip())
					insilcentrestate=False
	
				if insilcentrestate and not hmmdefs_line.startswith("<"):
					parameters_list.append(hmmdefs_line.rstrip())
				 
		else:
			new_hmmdefs.write(hmmdefs_line)

old_hmmdefs.close()
new_hmmdefs.close()


