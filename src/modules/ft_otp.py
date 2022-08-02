#!/usr/bin/python3.9
import random, sys, time

def	main(argv):

	if len(argv) > 1:
		OTPgenerator(int(argv[1]))
	else:
		print("Need input")
		return

def OTPgenerator(length) :

	OTP = ""
	for i in range(length) :
		OTP=OTP+str(random.choice(range(0,15)))
		print(OTP)
		time.sleep(1)
	return OTP

if __name__ == '__main__':
	main(sys.argv)