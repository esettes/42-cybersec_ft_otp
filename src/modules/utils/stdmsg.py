from modules.utils.bcolors import bcol
from datetime import datetime
from base64 import b32encode
from os import system
from modules.generateotp import GetDigits, TimeAwait
from argparse import RawTextHelpFormatter
import argparse

def	err_msg(s):
	print (bcol.FAIL + "[ERROR]: " + bcol.ENDC + s)

def load_msg(s):
	print (bcol.GREY + s + bcol.ENDC)

def	warn_msg(s):
	print (bcol.WARN + "[WARNING]: " + bcol.ENDC + s)

def success_msg(s):
	print (bcol.GREEN_B + "[OK] " + bcol.ENDC + s)

def info_msg(s):
	print(bcol.BLUE + "* " + bcol.ENDC + s)

def TryAgainPsswd():
	err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")

def MainArguments():
	head = bcol.BLUE + """
  _____ ___ _____ ____        ____            
 |_   _/ _ |_   _|  _ \      / ___| ___ _ __  
   | || | | || | | |_) _____| |  _ / _ | '_ \ 
   | || |_| || | |  __|_____| |_| |  __| | | |
   |_| \___/ |_| |_|         \____|\___|_| |_| """ + bcol.ENDC + """

Temporary one time password generator.


Usually steps:
\tCreate a master key:
\t[ ./ft_otp -r "My super secret master key 123456 super password" ]

\tGenerate tot-password:
\t[ ./ft_otp -k ft_otp.key ]

------------------------------------------------""" 
	parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=head)
	parser.add_argument('-g','--generate', metavar='<key>', default=None, help="[ -g <key> ] Recieves an hexadecimal key of at least 64 characters.")
	parser.add_argument('-r','--readablegen', metavar='<key>', default=None, help="[ -r <key> ] Recieves a string with any characters and formats it to hexadecimal.")
	parser.add_argument('-p','--passwd', action='store_true', help="[ -p ] Change the password.")
	parser.add_argument('-k','--key', metavar='<key>', default=None, help="[ -k <key> ] Generates a new temporaly password.")
	parser.add_argument('-v','--verbose', action='store_true', help="[ -v ] Show more info about generated totp.")
	args = parser.parse_args()
	return args

def GUI_OTP(totp, mykey):
	system("clear")
	head = """
  _____ ___ _____ ____        ____            
 |_   _/ _ |_   _|  _ \      / ___| ___ _ __  
   | || | | || | | |_) _____| |  _ / _ | '_ \ 
   | || |_| || | |  __|_____| |_| |  __| | | |
   |_| \___/ |_| |_|         \____|\___|_| |_|
	"""
	print(bcol.BLUE + head + bcol.ENDC)
	print(bcol.GREY + "author: iostancu" + bcol.ENDC)
	print(bcol.BLUE + "----------------------------------------------" + bcol.ENDC)
	print(bcol.GREY + "Hex secret: " + mykey)
	print("Base32 secret: " + b32encode(bytearray.fromhex(mykey)).decode('utf-8'))
	print("Digits: " + str(GetDigits()))
	print("TOTP model: SHA1")
	print("Step size: " + str(TimeAwait()))
	print("Start time: 1970/01/01, 00:00:00")
	print("Current time: " + datetime.now().strftime("%Y/%m/%d, %H:%M:%S") + bcol.ENDC)
	#print("Counter: {} ({})".format(hex(GetTotpCounter().decode()),GetTotpCounter().decode()))
	print(bcol.BLUE + "----------------------------------------------")
	print("TOTP: \n" + bcol.ENDC + totp)
	print(bcol.BLUE + "----------------------------------------------" )
	print("OATHTOOL TOTP: " + bcol.ENDC)#,end = '')
	system("oathtool --totp " + mykey)
	print(bcol.BLUE + "----------------------------------------------\n" + bcol.ENDC)