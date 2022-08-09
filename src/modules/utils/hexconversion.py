import subprocess

def ConvertToHex(mystr):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=mystr)
	hex_format = toHex.stdout.replace('\n', '')
	print(hex_format)
	return hex_format

def PrintOathtool(k):
	toprint = subprocess.run(["oathtool --totp"], stdout=subprocess.PIPE, text=True, input=k)
	p = toprint.stdout

	print("OATHTOOL: [ " + p + " ]")