#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from argparse import ArgumentParser

class SRDKRunError(Exception):
        pass

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir, followlinks=True):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


def make_symlink(name, uid):
	os.system("cd audio/wav && ln -s ../../../corpus/audio/" + name + "/wav/" + uid)

def prepare_audio(filename, corpusname, **args):

	os.system("rm -rf audio")
	os.system("mkdir -p audio/wav")

	if filename is not None:
		with open(filename, 'r') as f:
			for line in f:
				uid=line.rstrip('\n')	
				make_symlink(corpusname, uid)  	
	else:
		corpusdirinfo = get_directory_structure("../corpus/audio/" + corpusname)
                for user in corpusdirinfo[corpusname]["wav"]:
			make_symlink(corpusname, user)

	os.system("cp ../corpus/audio/" + corpusname + "/samples.txt .")

if __name__ == "__main__":

        parser = ArgumentParser(description="Sgript creu model acwstig gyda un gorchymun")

        parser.add_argument('-f', '--file', dest="filename", required=False, help="ffeil userids benodol")
	parser.add_argument('-n', '--name', dest="corpusname", required=True, help="Enw'r corpws lleferydd (e.e. Paldaruo)")
        parser.set_defaults(func=prepare_audio)
	
	args=parser.parse_args()

	try:
		args.func(**vars(args))
	except SRDKRunError as e:
		print ("\n**SRDK ERROR**\n")
		print (e)


