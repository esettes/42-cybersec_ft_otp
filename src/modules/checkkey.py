#!/usr/bin/python3.9
import modules.stdmsg as msg

def CheckValidKey(key):
	formatCheck = CheckValidFormat(key)
	lenCheck = CheckValidLenght(key)
	if formatCheck and lenCheck:
		msg.load_msg("Saving and encripting new key...")
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
		#msg.load_msg('Key <' + key + '> is a correct hexadecimal format')
		return True
	else:
		msg.err_msg('Key <' + key + '> is not correct formatted')
		return False

def EncryptKey(key):
	with open("ft_otp.key", "wb") as key_file:
		key_file.write(key)
		key_file.close()