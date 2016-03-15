#!/usr/bin/env python

import os, errno

for root, dirs, files in os.walk("."):

        path = root.split('/')

        for file in files:

		if ".wav" not in file:
			continue;

		if not file.endswith('.wav'):

			error_extension_start = file.index('.')
			newfilename = file[:error_extension_start] + ".wav"

			print "Cywiro / Correcting : ", file, newfilename
			
			os.rename(root + '/' + file, root + "/" + newfilename)
					


