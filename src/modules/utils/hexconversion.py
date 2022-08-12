import subprocess, binascii

def ConvertToHex(mystr):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=mystr)
	hex_format = toHex.stdout.replace('\n', '')
	print(hex_format)
	return hex_format
