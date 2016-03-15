#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pprint
from argparse import ArgumentParser


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
 
dirinfo = get_directory_structure("audio")
os.system("rm -rf results")

for user in dirinfo["audio"]["wav"]:
	uid=user

	print ("uid=" + uid)

	if dirinfo["audio"]["wav"][uid] is None:
		continue

	#n=len(dirinfo["audio"]["wav"][uid])
	#print n
	#if n > 42:
	os.system ("SRDK_Train.py -u=" + uid)	

