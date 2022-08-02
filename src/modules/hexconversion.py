import subprocess
from modules.checkkey import CheckValidKey, SaveKey
import modules.stdmsg as msg

def ConvertToHex(str):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=str)
	hex_format = toHex.stdout.replace('\n', '')
	if CheckValidKey(hex_format):
		msg.load_msg("save ft_otp.key")
		SaveKey(hex_format)
