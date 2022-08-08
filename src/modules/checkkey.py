import modules.utils.stdmsg as msg
import os.path
from modules.utils.globvars import keypath
from modules.cript import MasterKeyPass
from base64 import b32decode, b32encode

def CheckValidKey(key):
	formatCheck = CheckValidFormat(key)
	lenCheck = CheckValidLenght(key)
	if formatCheck and lenCheck:
		return True
	if lenCheck == False:
		msg.err_msg("The key " + key + " must be at least for 64 charcters length")
	if formatCheck == False:
		msg.err_msg("The key " + key + " must be formated to hexadecimal")
	return False

def CheckValidLenght(key):
	if len(key) < 64:
		return False
	else:
		return True

def CheckValidFormat(key):
	hexChars = set('0123456789abcdefABCDEF')
	if all((c in hexChars) for c in key):
		return True
	else:
		msg.err_msg('Key <' + key + '> is not correct formatted')
		return False

def WriteKey(key, usrPsswd):
	try:
		#byteUsrPsswd = bytes(usrPsswd, 'utf-8')
		#keyToWrite = b32encode(key.encode('utf-8'))
		#print("key to write in writeKey")
		#print(keyToWrite)
		#masterkeyPsswd = MasterKeyPass(usrPsswd)
		#crypt = masterkeyPsswd.encrypt(bytes.fromhex(key))
		with open(keypath, "wb") as key_file:
			key_file.write(key.encode())
	except Exception:
		msg.err_msg("Fail to write key")
		return

def ConfirmCreateNewKey():
	if os.path.exists(keypath):
		msg.warn_msg("Another key exist. This action will overwrite it and is irreversible. Are you sure you want to overwrite it? [y/n] : ")
		usrInput = str(input(""))
		if usrInput == 'n' or usrInput == 'N':
			print("cancel key-gen and return program")
			return False
		elif usrInput == 'y' or usrInput == 'Y':
			return True
		else:
			msg.err_msg("Please write 'y' or 'n'")
			ConfirmCreateNewKey()
	return True
