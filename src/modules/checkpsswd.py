import modules.stdmsg as msg
from getpass import getpass

def NewPsswd():
	usrInput = getpass("Write a new password: ")
	print("writed: " + usrInput)
	usrCheck = getpass("Write the same password again: ")
	print("writed: " + usrCheck)
	if usrInput != usrCheck:
		msg.err_msg("The passwords didn't match.Try again or press 'C' + [Enter] to cancel.")
		NewPsswd()
	elif usrInput == 'c' or usrCheck == 'c' or usrInput == 'C' or usrCheck == 'C':
		msg.load_msg("Canceled new key gen")
		return None
	elif usrInput == usrCheck:
		return usrInput
	return None
