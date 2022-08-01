#!/usr/bin/python3.9

def CheckValidKey(key):
	formatCheck = CheckValidFormat(key)
	lenCheck = CheckValidLenght(key)
	if formatCheck and lenCheck:
		print("Saving and encripting new key...")
		return True
	if lenCheck == False:
		print ("Key must be at least for 64 charcters length")
	if formatCheck == False:
		print ("Key must be formated to hexadecimal")
	return False

def CheckValidLenght(key):
	if len(key) < 64:
		return False
	else:
		return True

def CheckValidFormat(key):
	hexChars = set('0123456789abcdefABCDEF')
	if all((c in hexChars) for c in key):
		print('Key <' + key + '> is correct formatted')
		return True
	else:
		print('Key <' + key + '> is not correct formatted')
		return False

def EncryptKey(key):
	with open("ft_otp.key", "wb") as key_file:
		key_file.write(key)
		key_file.close()