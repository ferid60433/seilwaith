#!/usr/bin/env python
import sys

def main( fname ):

	file=open(fname,'r',encoding='utf-8')
	filelines=file.readlines()
	file.close()

	outfile=open(fname,'w',encoding='utf-8')
	filelines.sort()
	for line in filelines:
		outfile.write(line)
	outfile.close()


if __name__ == "__main__":
	main(sys.argv[1])

