from modules.utils.bcolors import bcol

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