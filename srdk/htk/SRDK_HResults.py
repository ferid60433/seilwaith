#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import subprocess
import pprint
import sqlite3
import math

from argparse import ArgumentParser

con=sqlite3.connect('paldaruo-metadata.db')
cur=con.cursor()

cur.execute("DROP TABLE IF EXISTS user_results")
cur.execute("CREATE TABLE user_results (uid PRIMARY KEY NOT NULL, word_accuracy NUMERIC NOT NULL, number_of_recordings NUMERIC NOT NULL)")

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
 
dirinfo = get_directory_structure("results")
os.system ("rm hresults.txt")

results=[]

for user in dirinfo["results"]:

	recoutfname = "results/" + user + "/recout.mlf"
        audiowavdirectory = 'audio/wav/' + user
	
	no_of_recordings = len([name for name in os.listdir(audiowavdirectory) if name.startswith('sample')])
	if os.path.isfile(recoutfname):

		hresult_output = subprocess.check_output("HResults -I words.mlf tiedlist " + recoutfname, shell=True)
		rateObj=re.search(r'WORD\:\ \%Corr=(.*),\ Acc', hresult_output,re.M|re.I)
		if rateObj:
			print recoutfname + " : " + rateObj.group(1) + ", " + str(no_of_recordings)	
			wordaccuracy = float(rateObj.group(1))
			if not math.isnan(wordaccuracy):
				result = (user, wordaccuracy, no_of_recordings)
			else:
				result = (user, 0.0,0)
		else:
			print recoutfname + " : 0.0, 0"
			result = (user, 0.0, 0)
	
			
		cur.execute("INSERT INTO user_results (uid, word_accuracy, number_of_recordings) VALUES (?,?,?)",result)
		con.commit()
	
con.close()

		#os.system("HResults -I words.mlf tiedlist " + recoutfname + " >> hresults.txt")
		#os.system("echo \"\n\n\" >> hresults.txt")
		
