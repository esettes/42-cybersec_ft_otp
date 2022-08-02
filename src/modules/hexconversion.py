#!/usr/bin/python3.9

import subprocess
from modules.checkkey import CheckValidKey
import modules.stdmsg as msg

def ConvertToHex(str):
	
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=str)
	#Check if transformation is correctly formatted and if is correct, save it in ft_otp-key
	hex_format = toHex.stdout.replace('\n', '')
	if CheckValidKey(hex_format):
		#Write key in ft_otp.key
		msg.load_msg("save otr_key")
	print (hex_format)