#!/usr/bin/python3.9

import sys, argparse
from modules.checkkey import ConfirmCreateNewKey
from modules.utils.hexconversion import ConvertToHex
from modules.workflow import ChangeMasterKey, ChangePassword, ObtainTOTP
import modules.utils.stdmsg as msg
from modules.utils.globvars import keypath
from argparse import RawTextHelpFormatter

def	main(argv):
	
	keysave = ""
	myverbose = False
	head = """
  _____ ___ _____ ____        ____            
 |_   _/ _ |_   _|  _ \      / ___| ___ _ __  
   | || | | || | | |_) _____| |  _ / _ | '_ \ 
   | || |_| || | |  __|_____| |_| |  __| | | |
   |_| \___/ |_| |_|         \____|\___|_| |_|

Temporary one time password generator.
------------------------------------------------
Usually steps:
\tCreate a master key:
[ ./ft_otp -rg "My super secret master key 123456 super password" ]

\tGenerate tot-password:
[ ./ft_otp -k modules/key/ft_otp.key ]
------------------------------------------------
	"""
	parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=head)
	parser.add_argument('-g','--generate', metavar='<key>', default=None, help="[ -g <key> ] Recieves an hexadecimal key of at least 64 characters.")
	parser.add_argument('-rg','--readablegen', metavar='<key>', default=None, help="[ -rg <key> ] Recieves a string with any characters and formats it to hexadecimal.")
	parser.add_argument('-p','--passwd', action='store_true', help="[ -p ] Change the password.")
	parser.add_argument('-k','--key', metavar='<key>', default=None, help="[ -k <key> ] Generates a new temporaly password.")
	parser.add_argument('-v','--verbose', action='store_true', help="[ -v ] Show more info about generated totp.")
	args = parser.parse_args()
	if args.verbose:
		myverbose = True
	if args.generate or args.readablegen:
		if ConfirmCreateNewKey():
			if args.generate != None and args.readablegen == None:
				keysave = args.generate
			if args.generate == None and args.readablegen != None:
				keysave = ConvertToHex(args.readablegen)
				print(keysave)
			if ChangeMasterKey(keysave):
				msg.success_msg("Master key changed successfuly.")
			else:
				msg.err_msg("Can't change master key")
		else:
			msg.load_msg("Abort master key modification.")
	if args.passwd:
		if ChangePassword():
			msg.success_msg("Password changed successfuly.")
		else:
			msg.load_msg("Abort password modification.")
	if args.key != None and args.readablegen == None and args.generate == None:
		if args.key == keypath or args.key == keypath[6:]:
			ObtainTOTP(args.key, myverbose)
		else:
			msg.err_msg('No such file or directory in "' + args.key + '"')
			print('Key would be in "modules/key/ft_otp.key"')
	return



if __name__ == '__main__':
	main(sys.argv)