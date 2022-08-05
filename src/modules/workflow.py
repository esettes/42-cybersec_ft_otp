from modules.globvars import keypath
from modules.checkpsswd import NewPsswd
import modules.stdmsg as msg
from modules.cript import CryptKey, DecriptKey
from modules.checkkey import CheckValidKey, WriteKey
from getpass import getpass
from os.path import exists

def ChangePassword():
	usrPsswd = getpass("Password: ")
	print ("pswd in ChangePassword: " )
	print(usrPsswd)
	if DecriptKey(usrPsswd.encode()):
		newPsswd = NewPsswd()
		if newPsswd != None:
			CryptKey(newPsswd.encode())
			return True
	elif usrPsswd == 'c' or usrPsswd == 'C':
		return False
	else:
		msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
		ChangePassword()


def ChangeMasterKey(key):
	if CheckValidKey(key):
		usrPsswd = getpass("Password: ")
		usrPsswd = usrPsswd.encode()
		if not exists(keypath):
			WriteKey(key)
			CryptKey(usrPsswd)
			print ("no existe")
			return True
		elif exists(keypath):
			if DecriptKey(usrPsswd):
				print("exists")
				WriteKey(key)
				CryptKey(usrPsswd)
				return True
	return False
