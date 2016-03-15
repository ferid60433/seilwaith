#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist

from argparse import ArgumentParser

def get_most_frequent_words(indirectory, outfile, count, **args):

	print (indirectory, outfile, count)

	corpus=PlaintextCorpusReader(indirectory,'.*\.txt')
	tokens=corpus.words()
	fdist=FreqDist(tokens)	
	most_freq=fdist.most_common(count)

	with open(outfile,'wb') as of:
		of.write(bytes('<s>\n','UTF-8'))
		of.write(bytes('</s>\n','UTF-8'))
		for word,frequency in most_freq:
			if word.isalpha():
				of.write(bytes(word+"\n",'UTF-8'))

if __name__ == "__main__":

	parser = ArgumentParser(description="Canfod y ffeiliau mwya cyffredin o fewn corpws")

	parser.add_argument('-d', '--directory', dest="indirectory", required=True, help="y ffolder sy'n cynnwys ffeiliau'r corpws")
	parser.add_argument('-o', '--out', dest="outfile", required=True, help="i ble dylid cadw'r ffeil wedi'i priflythrennu")
	parser.add_argument('-c', '--count', dest="count", type=int, required=True, help="sawl geiriau")
	parser.set_defaults(func=get_most_frequent_words)

	args=parser.parse_args()
	args.func(**vars(args))

