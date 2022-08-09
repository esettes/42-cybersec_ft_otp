import argparse

class OptArgs():
	def __init__(self):
		parser = argparse.ArgumentParser(description="*** TOTP generator ***")
		parser.add_argument('-g','--generate', metavar='<key>', default=None, help="[ -g <key> ] Recieves an hexadecimal key of at least 64 characters.")
		parser.add_argument('-rg','--readablegen', metavar='<key>', default=None, help="[ -rg <key> ] Recieves a string with any characters and formats it to hexadecimal.")
		parser.add_argument('-p','--passwd', action='store_true', help="[ -p ] Change the password.")
		parser.add_argument('-v','--verbose', action='store_true', help="[ -v ] Show more info about generated totp.")
		parser.add_argument('-k','--key', metavar='<key>', default=None, help="[ -k <key> ] Generates a new temporaly password.")
		self.args = parser.parse_args()

