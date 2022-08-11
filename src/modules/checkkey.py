import modules.utils.stdmsg as msg

def CheckValidKey(key):
	if key == None or key == "":
		return False
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
	if len(key) < 64:# or len(key) % 2 != 0:
		return False
	else:
		return True

def CheckValidFormat(key):
	hexChars = set('0123456789abcdefABCDEF')
	if all((c in hexChars) for c in key):
		return True
	else:
		#msg.err_msg('Key <' + key[-6:] + '...> is not correct formatted')
		return False

def WriteKey(object):
	try:
		with open(object.get_keypath(), "wb") as key_file:
			key_file.write(object.get_key().encode())
	except Exception:
		msg.err_msg("Fail to write key")
		return


