#!/usr/bin/env python

import sys, os, errno
from argparse import ArgumentParser
from subprocess import Popen, PIPE

kwargs = {'stdin': PIPE, 'stdout':PIPE, 'stderr':PIPE}

class SRDKRunError(Exception):
        pass

def create_codetrain(userid, **args):

	print userid

	f = open('codetrain.scp','w')

	if userid is not None:
		rootdir = "audio/wav/" + userid
		walk_and_create_codetrain(rootdir, f)	
	else:
		rootdir = "audio/wav"
		walk_and_create_codetrain(rootdir, f)
	
	f.close()

def walk_and_create_codetrain(rootdir, f):

	for root, dirs, files in os.walk(rootdir, followlinks=True):

        	path = root.split('/')

	        for file in files:

			mfcc_dir = root.replace('wav','mfcc').replace('./','')
			wavfile = root + '/' + file
			codetrain_line = wavfile.replace('./','') + ' ' + mfcc_dir + '/' + file.replace('.wav','.mfc')

			if ".wav" not in file:
				continue;

			if "silence_" in file:
				continue;
		
			print codetrain_line

			try:
				os.makedirs(mfcc_dir)
			except OSError as exc:
				if exc.errno == errno.EEXIST and os.path.isdir(mfcc_dir):
					pass
				else: 
					raise
		
			f.write(codetrain_line + os.linesep)


if __name__ == "__main__":

	parser = ArgumentParser(description="Sgript creu codetrain.scp ar gyfer HTK")
        parser.add_argument('-u', '--userid', dest="userid", required=False, help="userid cyfrannwr benodol")
        parser.set_defaults(func=create_codetrain)

        args=parser.parse_args()
        try:
                args.func(**vars(args))
        except SRDKRunError as e:
                print ("\n**SRDK ERROR**\n")
                print (e)

