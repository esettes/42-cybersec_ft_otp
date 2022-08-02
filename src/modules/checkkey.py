import modules.stdmsg as msg
import os.path

keypath = "/home/modules/key/ft_opt.key"

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

def SaveKey(key):
	if KeyExisting():
		WriteKey(key)
		print("Override key")
	else:
		print ("Abort key-gen")
	return True

def WriteKey(key):
	with open(keypath, "wb") as key_file:
		key_file.write(key.encode())
		key_file.close()

def KeyExisting():
	if os.path.exists(keypath):
		msg.warn_msg("Another key exist. This action will overwrite it and is irreversible. Are you sure you want to overwrite it? [y/n] : ")
		usrInput = input("")
		if usrInput == 'n' or usrInput == 'N':
			print("cancel key-gen and return program")
			return False
		elif usrInput == 'y' or usrInput == 'Y':
			return True
		else:
			print("Please write 'y' or 'n'")
			KeyExisting()