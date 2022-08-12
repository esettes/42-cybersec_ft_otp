from modules.utils.globvars import keypath
from modules.checkpsswd import NewPsswd, CheckPsswdLength
import modules.utils.stdmsg as msg
from modules.cript import CryptKey, DecriptKey
from modules.checkkey import CheckValidKey, WriteKey
from getpass import getpass
from os.path import exists
from modules.otpgen2 import TruncateTOTP2

def ChangePassword():
	usrPsswd = str(getpass("Password: "))
	if usrPsswd == 'c' or usrPsswd == 'C':
		return False
	if DecriptKey(usrPsswd.encode()) and CryptKey(usrPsswd.encode()):
		newPsswd = NewPsswd()
		if newPsswd != None and newPsswd != "":
			if DecriptKey(usrPsswd.encode()) and CryptKey(newPsswd.encode()):
				return True
	else:
		msg.TryAgainPsswd()
		ChangePassword()
	return False


def ChangeMasterKey(key):
	if CheckValidKey(key):
		usrPsswd = str(getpass("Password: "))
		if usrPsswd == 'c' or usrPsswd == 'C':
			return False
		if CheckPsswdLength(usrPsswd):
			if not exists(keypath):
				WriteKey(key, usrPsswd)
				if CryptKey(usrPsswd.encode()):
					return True
			elif exists(keypath):
				if DecriptKey(usrPsswd.encode()):
					WriteKey(key, usrPsswd)
					if CryptKey(usrPsswd.encode()):
						return True
				else:
					msg.TryAgainPsswd()
					ChangeMasterKey(key)
		else:
			print("Try again or press 'C' + [Enter] to cancel.")
			ChangeMasterKey(key)
	return False

def ObtainTOTP(key, verb):
	usrPsswd = str(getpass("Password: "))
	if DecriptKey(usrPsswd.encode()):
		with open(key, 'r') as mykey:
			readed = mykey.read()
			if CryptKey(usrPsswd.encode()):
				try:
					totp = TruncateTOTP2(readed)
			#if CryptKey(usrPsswd.encode()):
			#	try:
					if verb:
						msg.GUI_OTP(totp, readed)
					else:
						msg.info_msg(totp)
				except Exception:
					print("Cant print")
	else:
		msg.err_msg("Incorrect password or key didn't exist")
