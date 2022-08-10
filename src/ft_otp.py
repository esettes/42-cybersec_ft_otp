#!/usr/bin/python3.9

import sys
from modules.masterkey import MasterKey
import modules.utils.arguments as optArgs
from modules.masterkey import MasterKey
from modules.utils.hexconversion import ConvertToHex
from modules.workflow import ChangeMasterKey, ChangePassword, ObtainTOTP
import modules.utils.stdmsg as msg

def	main(argv):
	myverbose = False
	parse = optArgs.OptArgs()
	mkey = MasterKey()

	if parse.args.verbose:
		myverbose = True
	if parse.args.generate or parse.args.readablegen:
		if MasterKey.ConfirmCreateNewKey():
			if parse.args.generate != None and parse.args.readablegen == None:
				mkey.set_key(parse.args.generate)
			if parse.args.generate == None and parse.args.readablegen != None:
				mkey.set_key(ConvertToHex(parse.args.readablegen))
			if ChangeMasterKey(mkey):
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