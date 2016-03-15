#!/usr/bin/env python

import sys, os, errno

f = open('train.scp','w')

with open('pretrain.scp','r') as pretrain_file:
	
	for mfcc_file in pretrain_file:

		tmp_train_file = open('tmp_train.scp','w')
		tmp_train_file.write(mfcc_file)
		tmp_train_file.close()

		returncode = os.system('HERest -A -D -T 1 -C config -I phones0.mlf -t 250.0 150.0 1000.0 -S tmp_train.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm05 monophones0')

		if returncode == 0:
			f.write(mfcc_file)
		else: 
			print("HERest errors in mfcc_file {0}".format(mfcc_file))
	

f.close()
