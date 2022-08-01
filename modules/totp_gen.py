#!/usr/bin/python3.9

from base64 import b32decode, b32encode
from struct import pack, unpack
from hmac import new
from hashlib import sha1
import sys, re, argparse
from checkkey import CheckValidKey
from hexconversion import ConvertToHex

def	main(argv):
	parser = argparse.ArgumentParser(description="*** TOTP generator ***")
	parser.add_argument('-g','--generate', metavar='<key>', default=None, help="[ -g <key> ] Recieves an hexadecimal key of at least 64 characters.")
	parser.add_argument('-rg','--readablegen', metavar='<key>', default=None, help="[ -rg <key> ] Recieves a string and formats it to hexadecimal.")
	args = parser.parse_args()
	if args.generate != None and args.readablegen == None:
		CheckValidKey(args.generate)
	if args.generate == None and args.readablegen != None:
		ConvertToHex(args.readablegen)


if __name__ == '__main__':
	main(sys.argv)