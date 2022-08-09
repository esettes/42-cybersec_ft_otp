#!/usr/bin/python3.9

import sys, argparse
import modules.utils.arguments as optArgs
from modules.checkkey import ConfirmCreateNewKey
from modules.utils.hexconversion import ConvertToHex
from modules.workflow import ChangeMasterKey, ChangePassword, ObtainTOTP
import modules.utils.stdmsg as msg

def	main(argv):
	keysave = ""
	myverbose = False
	parse = optArgs.OptArgs()
	if parse.args.verbose:
		myverbose = True
	if parse.args.generate or parse.args.readablegen:
		if ConfirmCreateNewKey():
			if parse.args.generate != None and parse.args.readablegen == None:
				keysave = parse.args.generate
			if parse.args.generate == None and parse.args.readablegen != None:
				keysave = ConvertToHex(parse.args.readablegen)
			if ChangeMasterKey(keysave):
				msg.success_msg("Master key changed successfuly.")
		else:
			msg.load_msg("Abort master key modification.")
	if parse.args.passwd:
		if ChangePassword():
			msg.success_msg("Password changed successfuly.")
		else:
			msg.load_msg("Abort password modification.")
	if parse.args.key != None and parse.args.readablegen == None and parse.args.generate == None:
		ObtainTOTP(parse.args.key, myverbose)
	return

if __name__ == '__main__':
	main(sys.argv)