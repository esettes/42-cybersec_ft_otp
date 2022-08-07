import subprocess

def ConvertToHex(str):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=str)
	hex_format = toHex.stdout.replace('\n', '')
	print(hex_format)
	return hex_format
