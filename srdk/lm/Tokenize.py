#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import sys, os, errno, re
from argparse import ArgumentParser

def tokenize_file(infile, outfile, reversefile, **args):

	out_file = open(outfile,'wb+')
	out_reverse_file = open(reversefile,'wb+')
	
	with open(infile,'r', encoding='utf-8') as in_file:
		for line in in_file.readlines():
			upper=line.rstrip('\n').upper()
			tokens = tuple(re.findall(r"(?:^|\b).(?:\B.)*",upper))

			upper=[]
			for token in tokens:
				if token.isalpha():
					upper.append(token)

			out_file.write(bytes("<s> " + ' '.join(upper) + " </s>\n","UTF-8"))
			out_reverse_file.write(bytes("<s> " + ' '.join(upper[::-1]) + " </s>\n","UTF-8")) 
	
	out_file.close()
	out_reverse_file.close()

if __name__ == "__main__":
	
	parser = ArgumentParser(description="Trosi ffeil i gyd i upper, ei docyneiddio a'i baratoi ar gyfer hyfforddi model iaith")

	parser.add_argument('-i', '--in', dest="infile", required=True, help="y ffeil ar gyfer priflythrennu")
	parser.add_argument('-o', '--out', dest="outfile", required=True, help="i ble dylid cadw'r ffeil wedi'i priflythrennu")
	parser.add_argument('-r', '--reverse', dest="reversefile", required=True, help="y ffeil ar gyfer creu model reverse n-gram")
	parser.set_defaults(func=tokenize_file)

	args=parser.parse_args()
	args.func(**vars(args))

