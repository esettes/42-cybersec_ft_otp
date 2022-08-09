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
		if newPsswd != None:
			if DecriptKey(usrPsswd.encode()) and CryptKey(newPsswd.encode()):
				return True
	else:
		msg.TryAgainPsswd()
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
					msg.TryAgainPsswd()
					ChangeMasterKey(key)
		else:
			msg.TryAgain()
			ChangeMasterKey(key)
	return False

def ObtainTOTP(key, verb):
	usrPsswd = str(getpass("Password: "))
	try:
		if DecriptKey(usrPsswd.encode()):
			with open(key, 'r') as mykey:
				readed = mykey.read()
				#try:
				#	PrintOathtool(readed)
				#except Exception:
					#msg.err_msg("Cant print oathtool")
				totp = TruncateTOTP2(readed)
				if CryptKey(usrPsswd.encode()):
					try:
						if verb:
							msg.GUI_OTP(totp)
						else:
							msg.info_msg(totp)
					except Exception:
						print("Cant print")
	except Exception:
		msg.err_msg("Can't truncate TOTP")
