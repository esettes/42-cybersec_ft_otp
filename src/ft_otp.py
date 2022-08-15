#!/usr/bin/python3.9

from modules.checkkey import ConfirmCreateNewKey, KeyExist
from modules.utils.hexconversion import ConvertToHex
from modules.workflow import ChangeMasterKey, ChangePassword, ObtainTOTP
import modules.utils.stdmsg as msg
import sys

def	main(argv):
	keysave = ""
	existing_keypath = KeyExist()
	myverbose = False
	args = msg.MainArguments()
	if args.verbose:
		myverbose = True
	if args.generate or args.readablegen:
		if ConfirmCreateNewKey(existing_keypath):
			if args.generate != None and args.readablegen == None:
				keysave = args.generate
			if args.generate == None and args.readablegen != None:
				keysave = ConvertToHex(args.readablegen)
			if ChangeMasterKey(keysave, existing_keypath):
				msg.success_msg("Master key changed successfuly.")
			else:
				msg.err_msg("Can't change master key")
		else:
			msg.load_msg("Abort master key modification.")
	if args.passwd:
		if existing_keypath != None:
			if ChangePassword(existing_keypath):
				msg.success_msg("Password changed successfuly.")
			else:
				msg.load_msg("Abort password modification.")
		else:
			msg.err_msg("Any password is set for any key. Create a master key before change password.")
	if args.key != None and args.readablegen == None and args.generate == None:
		ObtainTOTP(args.key, myverbose)
	return

if __name__ == '__main__':
	main(sys.argv)