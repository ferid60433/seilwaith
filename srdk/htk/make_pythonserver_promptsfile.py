#!/usr/bin/env python

import sys, re, os, errno

f = open('prompts.py','w')
r = open('samples_tmp.txt','r')

f.write('#!/usr/bin/env python' + os.linesep)
f.write('#encoding: UTF-8' + os.linesep)
f.write('PROMPTS = [' + os.linesep)

for line in r.readlines():
	fields = re.split('\. ', line)
	print fields
	prompt = fields[1].rstrip()
	words = re.split('\ ', prompt)
	prompt = ", ".join(words)	
	f.write('	{"identifier": "sample' + fields[0] + '", "text": u"{' + prompt + '"},' + os.linesep)

f.write(']' + os.linesep)

f.close()


