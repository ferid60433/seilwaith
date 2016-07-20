#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re
import subprocess
import pprint
import sqlite3, wave
import math

from argparse import ArgumentParser

con=sqlite3.connect('paldaruo-metadata.db')
cur=con.cursor()

cur.execute("DROP TABLE IF EXISTS user_results")
cur.execute("DROP TABLE IF EXISTS wavfiles")
cur.execute("CREATE TABLE user_results (uid PRIMARY KEY NOT NULL, word_accuracy NUMERIC NOT NULL, number_of_recordings NUMERIC NOT NULL)")
cur.execute("CREATE TABLE wavfiles (uid NOT NULL, filename TEXT, duration REAL)")


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


def get_wav_info(uid, audiodir):
    wavlist = []
    for root, dirs, files in os.walk(audiodir):
	for file in files:
		if ".wav" not in file:
			continue

		if "silence_" in file:
			continue

                wavfile = root + '/' + file
                print '\t' + wavfile

                duration=0.0
                try:
                    waveobject=wave.open(wavfile, 'r')
                    nframes=waveobject.getnframes()
                    rate=waveobject.getframerate()
                    duration=nframes/float(rate)
                    waveobject.close()

                    wavlist.append((uid, file, duration))

                except OSError as exc:
                    print exc
                    continue

    cur.executemany("INSERT INTO wavfiles (uid,filename,duration) VALUES (?,?,?);", wavlist)
    con.commit() 


dirinfo = get_directory_structure("results")
os.system ("rm hresults.txt")

results=[]

for user in dirinfo["results"]:

	recoutfname = "results/" + user + "/recout.mlf"
        audiowavdirectory = 'audio/wav/' + user

        get_wav_info(user, audiowavdirectory)
 	
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
		
