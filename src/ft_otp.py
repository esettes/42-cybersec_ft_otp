#!/usr/bin/python3.9

import sys
from modules.masterkey import MasterKey, default_keypath
import modules.utils.arguments as optArgs
from modules.utils.hexconversion import ConvertToHex
from modules.workflow import ChangeMasterKey, ChangePassword, ObtainTOTP
import modules.utils.stdmsg as msg

def	main(argv):
	myverbose = False
	parse = optArgs.OptArgs()
	mkey = MasterKey("123456789", default_keypath)
	#if mkey.get_keypath() == "":
	#	mkey.set_keypath(default_keypath)
	print (mkey.get_key())
	if parse.args.verbose:
		myverbose = True
	if parse.args.generate or parse.args.readablegen:
		if MasterKey.ConfirmCreateNewKey():
			if parse.args.generate != None and parse.args.readablegen == None:
				mkey.set_key(parse.args.generate)
			if parse.args.generate == None and parse.args.readablegen != None:
				mkey.set_key(ConvertToHex(parse.args.readablegen))
			print (mkey.get_key())
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
		mkey.set_keypath(parse.args.key)
		
		print(mkey.get_keypath())
		ObtainTOTP(mkey.get_keypath(), myverbose)
	return

if __name__ == '__main__':
	main(sys.argv)