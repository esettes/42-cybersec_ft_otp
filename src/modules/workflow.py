from modules.checkpsswd import NewPsswd, CheckPsswdLength
import modules.utils.stdmsg as msg
from modules.cript import CryptKey, DecriptKey
from modules.checkkey import CheckValidKey, WriteKey
from getpass import getpass
from modules.generateotp import TruncateTOTP2
from modules.checkkey import default_keypath

def ChangePassword(existing_key):
	usrPsswd = str(getpass("Password: "))
	if usrPsswd == 'c' or usrPsswd == 'C':
		return False
	if DecriptKey(usrPsswd.encode(), existing_key) and CryptKey(usrPsswd.encode(), existing_key):
		newPsswd = NewPsswd()
		if newPsswd != None and newPsswd != "":
			if DecriptKey(usrPsswd.encode(), existing_key) and CryptKey(newPsswd.encode(), existing_key):
				return True
	else:
		msg.err_msg("Incorrect password.")
	return False


def ChangeMasterKey(key, existing_key):
	if CheckValidKey(key):
		usrPsswd = str(getpass("Password: "))
		if CheckPsswdLength(usrPsswd):
			if existing_key == None:
				WriteKey(key, default_keypath)
				if CryptKey(usrPsswd.encode(), default_keypath):
					return True
			elif existing_key != None:
				if DecriptKey(usrPsswd.encode(), existing_key):
					WriteKey(key, existing_key)
					if CryptKey(usrPsswd.encode(), existing_key):
						return True
				else:
					msg.err_msg("Incorrect password.")
					return False
		else:
			return False
	return False

def ObtainTOTP(key, verb):
	try:
		with open(key, 'r') as mykey:
			readed = mykey.read()
	except Exception:
		msg.err_msg('Key must be a file not a string.(ft_otp.key)')
		return
	usrPsswd = str(getpass("Password: "))
	if DecriptKey(usrPsswd.encode(), key):
		with open(key, 'r') as mykey:
			readed = mykey.read()
		if CryptKey(usrPsswd.encode(), key):
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
		msg.err_msg("Incorrect password.")
		return
