from modules.utils.globvars import keypath
from modules.otpgen import GenerateTOTP
from modules.checkpsswd import NewPsswd
import modules.utils.stdmsg as msg
from modules.cript import CryptKey, DecriptKey
from modules.checkkey import CheckValidKey, WriteKey
from getpass import getpass
from os.path import exists
from modules.checkpsswd import CheckPsswdLength
from modules.otpgen2 import TruncateTOTP2
import ipdb

def ChangePassword():
	usrPsswd = str(getpass("Password: "))
	if usrPsswd == 'c' or usrPsswd == 'C':
		return False
	if DecriptKey(usrPsswd.encode()) and CryptKey(usrPsswd.encode()):
		newPsswd = NewPsswd()
		if newPsswd != None:
			if DecriptKey(usrPsswd.encode()) and CryptKey(newPsswd.encode()):
				return True
	else:
		msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
		ChangePassword()


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
					msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
					ChangeMasterKey(key)
		else:
			print("Try again or press 'C' + [Enter] to cancel.")
			ChangeMasterKey(key)
	return False

def ObtainTOTP(key):
	usrPsswd = str(getpass("Password: "))
	#ipdb.set_trace()
	if DecriptKey(usrPsswd.encode()):
		print(key)
		with open(key, 'r') as mykey:
			readed = mykey.read()
			readed.strip()
			print("mykey readed: ")
			print(readed)
			#totp = GenerateTOTP(readed)
			totp = TruncateTOTP2(readed)
			if CryptKey(usrPsswd.encode()):
				msg.info_msg(totp)
	
	#keyToWrite = b32decode(r_file.encode('utf-8'))
			#decrypt = masterkeyPsswd.decrypt(keyToWrite)