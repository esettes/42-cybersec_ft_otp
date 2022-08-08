import base64, time, math, hmac, hashlib
from hashlib import sha1

def GetTotpCounter():
	timeNow = math.floor(time.time())
	timeAwait = 30
	count = math.floor(timeNow / timeAwait)
	return count.to_bytes(8, byteorder='big')

def TruncateTOTP2(key):
	print("keyyyyyy: ")
	print(key)
	mykey = base64.b64decode(key)
	
	print(mykey)
	counter = GetTotpCounter()
	otpmac = hmac.new(mykey, counter, hashlib.sha1).digest()
	offset = otpmac[19] & 15
	totp = str(int.from_bytes(otpmac[offset : offset + 4], 'big', signed=False))
	return totp[-6:]

#def GenerateTOTP2(key):
