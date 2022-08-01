#!/usr/bin/python3.9
#!/usr/bin/python3.9

from base64 import b32decode, b32encode
from struct import pack, unpack
from hmac import new
from hashlib import sha1
import sys, re

def	main(argv):

#	if len(argv) > 1:
		get_h()
#	else:
#		print("Need input")
#		return


#def	get_h(hexakey, count):
def	get_h():	


#	miss_pad = len(hexakey) % 4	
#	if miss_pad:
#		hexakey += '\x07' * (4 - miss_pad)
	key = b32decode('68 65 79 20 68 6f 6c 61', True)
	print (key)

if __name__ == '__main__':
	main(sys.argv)