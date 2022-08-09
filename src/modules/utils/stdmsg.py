from modules.otpgen2 import GetDigits, TimeAwait
from modules.utils.bcolors import bcol
from datetime import datetime

def	err_msg(s):
	print (bcol.FAIL + "[ERROR]: " + bcol.ENDC + s)

def load_msg(s):
	print (bcol.GREY + s + bcol.ENDC)

def	warn_msg(s):
	print (bcol.WARN + "[WARNING]: " + bcol.ENDC + s)

def success_msg(s):
	print (bcol.GREEN_B + "[OK] " + bcol.ENDC + s)

def debug_msg(s, v):
	print(bcol.BACKGR + "[DEBUG] " + s + bcol.ENDC)
	print(v)

def info_msg(s):
	print(bcol.BLUE + "* " + bcol.ENDC + s)

def TryAgainPsswd():
	err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")

def TryAgain():
	print("Try again or press 'C' + [Enter] to cancel.")

def GUI_OTP(totp):
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
	print(bcol.GREY + "Digits: " + str(GetDigits()))
	print("Step size: " + str(TimeAwait()))
	print("Start time: 1970/01/01, 00:00:00")
	print("Current time: " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + bcol.ENDC)
	#print("Counter: " + GetTotpCounter().decode() )
	print(bcol.BLUE + "----------------------------------------------")
	print("TOTP: " + bcol.ENDC + totp)
	print(bcol.BLUE + "----------------------------------------------" + bcol.ENDC)
