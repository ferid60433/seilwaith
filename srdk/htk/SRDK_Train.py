#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import traceback
from argparse import ArgumentParser

class SRDKRunError(Exception):
	
	def __init__(self, message):
		self.msg = message

def run_commands(cmds):
        for cmd in cmds:
                cmd = u" ".join(cmd)
                print("Rhedeg %s" % cmd)
                returncode = os.system(cmd)
		try:
	                if returncode != 0:
        	                exception_str = ["Problem yn rhedeg y gorchymyn:", "      %s" % cmd]
                	        raise SRDKRunError(u"\n".join(exception_str))
		except SRDKRunError, arg:
			print 'Exception:', arg.msg

def train_singleuser(userid, **args):
        """Hyfforddi model acwstig HTK / Train HTK acoustic model"""
       	srdk_cmds = []

	print "SRDK_Train : %s" % userid

	if userid :
		srdk_cmds.append(["rm -rf results/" + userid])
		srdk_cmds.append(["mkdir -p results/" + userid])

	srdk_cmds.append(["SRDK_2_PronunciationDictionary"])
	srdk_cmds.append(["SRDK_4_Transcriptions"]) 
	
	if userid:
		srdk_cmds.append(["SRDK_5_CodingAudioData " + userid ])
	else:
		srdk_cmds.append(["SRDK_5_CodingAudioData"])

	srdk_cmds.append(["SRDK_6_FlatStart"])
	srdk_cmds.append(["SRDK_7_SilenceModels"])
	srdk_cmds.append(["SRDK_8_Realign"])
	srdk_cmds.append(["SRDK_9_Triphones"])
	srdk_cmds.append(["SRDK_10_TiedStateTriphones"])
	srdk_cmds.append(["SRDK_11_TestModels"])

	if userid:
		srdk_cmds.append(["cp recout.mlf results/" + userid])
	
	#srdk_cmds.append(["SRDK_12_Release"])

        run_commands(srdk_cmds)

if __name__ == "__main__":

        parser = ArgumentParser(description="Sgript creu model acwstig gyda un gorchymun")

        parser.add_argument('-u', '--userid', dest="userid", required=False, help="userid cyfrannwr benodol")
        parser.set_defaults(func=train_singleuser)

	args=parser.parse_args()
	try:
		args.func(**vars(args))
	except SRDKRunError as e:
		print ("\n**SRDK ERROR**\n")
		print (e)

