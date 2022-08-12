import modules.utils.stdmsg as msg
import os.path
from modules.utils.globvars import keypath

def CheckValidKey(key):
	formatCheck = CheckValidFormat(key)
	lenCheck = CheckValidLenght(key)
	if formatCheck and lenCheck:
		return True
	if lenCheck == False:
		msg.err_msg("The key " + key[-6:] + "... must be even and at least for 64 charcters length")
	if formatCheck == False:
		msg.err_msg("The key " + key[-6:] + "... must be formated to hexadecimal")
	return False

def CheckValidLenght(key):
	if len(key) < 64 or len(key) % 2 != 0:
		return False
	else:
		return True

def CheckValidFormat(key):
	hexChars = set('0123456789abcdefABCDEF')
	if all((c in hexChars) for c in key):
		return True
	else:
		return False

def WriteKey(key, usrPsswd):
	try:
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
			return False
		elif usrInput == 'y' or usrInput == 'Y':
			return True
		else:
			msg.err_msg("Please write 'y' or 'n'")
			ConfirmCreateNewKey()
	return True
