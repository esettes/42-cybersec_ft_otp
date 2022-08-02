#!/usr/bin/python3.9

import subprocess
from modules.checkkey import CheckValidKey, SaveKey
import modules.stdmsg as msg

def ConvertToHex(str):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=str)
	hex_format = toHex.stdout.replace('\n', '')
	if CheckValidKey(hex_format):
		#Write key in ft_otp.key
		msg.load_msg("save ft_otp.key")
		SaveKey(hex_format)
	print (hex_format)