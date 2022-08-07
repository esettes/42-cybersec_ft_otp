#!/usr/bin/python3.9
import hashlib
import random, time, math, hmac

def OTPgenerator():
	OTP = ""
	length = 5
	for i in range(length) :
		OTP=OTP+str(random.choice(range(0,15)))
		print(OTP)
		time.sleep(1)
	return OTP

def TruncateTOTP(totpHmac):
	binConvert = bin(int(totpHmac.hexdigest(), base=16))
	base10Ref = binConvert[-4:] # Last 4 bits like an integer reference
	offset = int(base10Ref, base=2)
	get32Bits = binConvert[offset * 8 : offset * 8 + 32]
	totp = str(int(get32Bits, base=2))
	return totp[-6:]


def GenerateTOTP(key):
	timeNow = math.floor(time.time())
	timeAwait = 30
	totp = math.floor(timeNow / timeAwait)
	totpHash = hmac.new(bytes(key, encoding="utf-8"),
		totp.to_bytes(length=8, byteorder="big"),
		hashlib.sha256, )
	
	return TruncateTOTP(totpHash)
