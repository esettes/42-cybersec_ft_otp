import subprocess, binascii

def ConvertToHex(mystr):
	toHex = subprocess.run(["xxd", "-p"], stdout=subprocess.PIPE, text=True, input=mystr)
	hex_format = toHex.stdout.replace('\n', '')
	print(hex_format)
	return hex_format

def ConvertToHex_HEXLIF(mystr):
	str_val = mystr.encode('utf-8', errors='strict')
	print(str_val)
	hex_val = binascii.hexlify(str_val).decode('utf-8')
	hex_format = hex_val.strip()
	print(hex_format)
	return hex_format

def PrintOathtool(k):
	toprint = subprocess.run(["oathtool --totp"], stdout=subprocess.PIPE, text=True, input=k)
	p = toprint.stdout

	print("OATHTOOL: [ " + p + " ]")