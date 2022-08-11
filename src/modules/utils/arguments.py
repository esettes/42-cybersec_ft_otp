import argparse
from argparse import RawTextHelpFormatter

class OptArgs():
	def __init__(self):
		head = """
  _____ ___ _____ ____        ____            
 |_   _/ _ |_   _|  _ \      / ___| ___ _ __  
   | || | | || | | |_) _____| |  _ / _ | '_ \ 
   | || |_| || | |  __|_____| |_| |  __| | | |
   |_| \___/ |_| |_|         \____|\___|_| |_|

Temporary one time password generator.

------------------------------------------------
Usually steps:
\tCreate a master key:
[ ./ft_otp -rg "My super secret master key 123456 super password" ]

\tGenerate tot-password:
[ ./ft_otp -k modules/key/ft_otp.key ]
------------------------------------------------
	"""
		parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter, description=head)
		parser.add_argument('-g','--generate', metavar='<key>', default=None, help="[ -g <key> ] Recieves an hexadecimal key of at least 64 characters.")
		parser.add_argument('-rg','--readablegen', metavar='<key>', default=None, help="[ -rg <key> ] Recieves a string with any characters and formats it to hexadecimal.")
		parser.add_argument('-p','--passwd', action='store_true', help="[ -p ] Change the password.")
		parser.add_argument('-v','--verbose', action='store_true', help="[ -v ] Show more info about generated totp.")
		parser.add_argument('-k','--key', metavar='<key>', default=None, help="[ -k <key> ] Generates a new temporaly password.")
		self.args = parser.parse_args()

