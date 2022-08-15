import modules.utils.stdmsg as msg
global default_keypath
default_keypath = '/home/ft_otp.key'

import glob

def KeyExist():
	for file in glob.glob(r'/home/**/ft_otp.key', recursive=True):
		if file:
			return file
		else:
			return None

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

def WriteKey(key, existing_key):
	try:
		with open(existing_key, "wb") as key_file:
			key_file.write(key.encode())
	except Exception:
		msg.err_msg("Fail to write key")
		return

def ConfirmCreateNewKey(existing_key):
	if existing_key != None:
		msg.warn_msg("Another key exist. This action will overwrite it and is irreversible. Are you sure you want to overwrite it? [y/n] : ")
		usrInput = str(input(""))
		if usrInput == 'n' or usrInput == 'N':
			return False
		elif usrInput == 'y' or usrInput == 'Y':
			return True
		else:
			msg.err_msg("Please write 'y' or 'n'")
			ConfirmCreateNewKey(existing_key)
	return True
