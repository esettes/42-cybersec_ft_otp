from textwrap import fill
from modules.globvars import keypath, psswd
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import modules.stdmsg as msg
import base64, os

def CryptKey(usrPsswd):
	masterkeyPsswd = MasterKeyPass(usrPsswd)
	try:
		with open(keypath, 'rb') as o_file:
			r_file = o_file.read()
			crypt = masterkeyPsswd.encrypt(r_file)
		with open(keypath, 'wb') as crypt_file:
			crypt_file.write(crypt)
	except Exception:
		msg.err_msg("Couldn't encript key")
		return False
	return True

def DecriptKey(usrPsswd):
	masterkeyPsswd = MasterKeyPass(usrPsswd)
	try:
		with open(keypath, 'rb') as o_file:
			r_file = o_file.read()
			decrypt = masterkeyPsswd.decrypt(r_file)
			with open(keypath, 'wb') as crypt_file:
				crypt_file.write(decrypt)
	except Exception:
		msg.err_msg("Couldn't decript key")
		return False
	return True

def MasterKeyPass(usrPsswd):
	print(usrPsswd)
	psswdLen = len(usrPsswd)
	if psswdLen < 16:
		fillPsswd = usrPsswd.zfill(16 - psswdLen)
	usrBytes = fillPsswd[:16]
	print(usrBytes)
	# Derivating key
	kdf = PBKDF2HMAC (algorithm=hashes.SHA256(), length=32, salt=usrBytes, iterations=1000,)
	msg.debug_msg("kdf: ")
	print(kdf)
	key = base64.urlsafe_b64encode(kdf.derive(usrBytes))
	msg.debug_msg("kdf: ")
	print(key)
	fer = Fernet(key)
	return fer