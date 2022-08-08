import base64, time, math, hmac
from hashlib import sha1

def GetTotpCounter():
	timeNow = math.floor(time.time())
	timeAwait = 30
	count = math.floor(timeNow / timeAwait)
	return count

def GetHotp(key):
	key = base64.b32decode(key, True)
	counter = GetTotpCounter()
	opthash = hmac.new(key, 
		counter,
		digest=sha1)
