#!/usr/bin/python3.9

import subprocess

def ConvertToHex(str):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=str)
	print (toHex.stdout)