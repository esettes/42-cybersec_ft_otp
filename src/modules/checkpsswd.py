from modules.globvars import psswd
import modules.stdmsg as msg
from getpass import getpass

def DecriptionPsswd():
	with open(psswd) as p:
		mainPsswd = p.read()
	print(mainPsswd)
	return mainPsswd

def RequireUnlockPsswd():
	usrPsswd = getpass("Password: ")
	mainPsswd = DecriptionPsswd()
	print("Passwd in file: " +  mainPsswd)
	if usrPsswd == mainPsswd:
		print ("Correct psswd, unlock")
		return True
	elif usrPsswd == 'c' or usrPsswd == 'C':
		return False
	else:
		msg.err_msg("Incorrect password. Try again or press 'C' + [Enter] to cancel.")
		RequireUnlockPsswd()
	return False

def NewPsswd():
	usrInput = input("Write a new password: ")
	usrCheck = input("Write the same password again: ")
	if usrInput != usrCheck:
		msg.err_msg("The passwords didn't match.Try again or press 'C' + [Enter] to cancel.")
		NewPsswd()
	elif usrInput == 'c' or usrCheck == 'c' or usrInput == 'C' or usrCheck == 'C':
		msg.load_msg("Canceled new key gen")
		return
	elif usrInput == usrCheck:
		print("Unlock the old key before")
		print("Save the new password, and encrypt the file")
		return True
	return False
