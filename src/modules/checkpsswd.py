import modules.stdmsg as msg
from getpass import getpass

def NewPsswd():
	usrInput = getpass("Write a new password: ")
	print("writed: " + usrInput)
	if usrInput == 'c' or usrInput == 'C':
		msg.load_msg("Canceled new key gen")
		return None
	if CheckPsswdLength(usrInput):
		usrCheck = getpass("Write the same password again: ")
		print("writed: " + usrCheck)
		if usrInput != usrCheck:
			msg.err_msg("The passwords didn't match.Try again or press 'C' + [Enter] to cancel.")
			NewPsswd()
		elif usrInput == usrCheck:
			return usrInput
	else:
		print("Try again or press 'C' + [Enter] to cancel.")
		NewPsswd()
	return None

def CheckPsswdLength(psswd):
	if len(psswd) < 6 or len(psswd) > 16:
		msg.err_msg("Password would be with 6 minimum characters and max 16")
		return False
	else:
		return True