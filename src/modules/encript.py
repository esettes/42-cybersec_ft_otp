from modules.globvars import keypath, psswd
from cryptography.fernet import Fernet
import modules.stdmsg as msg

def CryptKey(psswd):
	try:
		with open(psswd, "rb") as mykey:
			psswd = mykey.read()
		k = Fernet(psswd)
	except Exception:
		msg.err_msg("Couldn't read password file")
		return False
	try:
		with open(keypath, 'rb') as o_file:
			r_file = o_file.read()
			crypt = k.encrypt(r_file)
		with open(keypath, 'wb') as crypt_file:
			crypt_file.write(crypt)
	except Exception:
		msg.err_msg("Couldn't encript key")
		return False
	return True