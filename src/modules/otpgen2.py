from os.path import exists
import time, hmac, hashlib, struct
from modules.utils.globvars import keypath
import modules.utils.stdmsg as msg

def GetDigits():
	digits = 6
	return digits

def TimeAwait():
	timeAwait = 30
	return timeAwait

def TimeNow():
	t = int(time.time())
	return t

def GetTotpCounter():
	timeNow = int(time.time())
	timeAwait = 30
	count = int(timeNow / timeAwait)
	return struct.pack('>Q', count)

def TruncateTOTP2(mykey):
	if exists(keypath):
		counter = GetTotpCounter()
		otpmac = hmac.new(bytearray.fromhex(mykey), counter, hashlib.sha1).digest()
		offset = otpmac[-1] & 15
		totp = str(struct.unpack('>L', otpmac[offset : offset + 4])[0] & 0x7fffffff )
		return totp[-6:]
	else:
		msg.err_msg("Incorrect path (modules/key/ft_otp.key) or file didn't exists")

