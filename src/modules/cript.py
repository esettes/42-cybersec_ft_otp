#!/usr/bin/python3.9
from modules.globvars import keypath
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
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
		#msg.err_msg("Couldn't encript key")
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
		#msg.err_msg("Couldn't decript key")
		return False
	return True

def MasterKeyPass(usrPsswd):
	salt = os.urandom(16)
	salt = bytes.fromhex("6a38")
	# Derivating key
#	try:
	kdf = PBKDF2HMAC (algorithm=hashes.SHA256, length=32, salt=salt, iterations=39000,)
	key = base64.urlsafe_b64encode(kdf.derive(usrPsswd))
	fer = Fernet(key)
	return fer
#	except Exception:
#		msg.err_msg("Can't create key")
#	return None

