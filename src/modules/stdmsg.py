from modules.bcolors import bcol

def	err_msg(str):
	print (bcol.FAIL + "[ERROR]: " + bcol.ENDC + str)

def load_msg(str):
	print (bcol.GREY + str + bcol.ENDC)