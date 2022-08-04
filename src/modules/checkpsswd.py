from modules.globvars import psswd
import modules.stdmsg as msg

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
		return usrInput
	return None
