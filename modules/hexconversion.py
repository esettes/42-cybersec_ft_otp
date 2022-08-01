#!/usr/bin/python3.9

import subprocess

def ConvertToHex(str):
	toHex = subprocess.run(["xxd", "-p"], input=str)
	print (toHex)