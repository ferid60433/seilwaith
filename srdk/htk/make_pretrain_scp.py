#!/usr/bin/env python

import sys, os, errno
from subprocess import Popen, PIPE

f = open('pretrain.scp','w')

with open('codetrain.scp','r') as codetrain_file:
	for codetrain_line in codetrain_file:
		wav_file, mfcc_file = codetrain_line.split()
		f.write("{0}\n".format(mfcc_file))

f.close()
