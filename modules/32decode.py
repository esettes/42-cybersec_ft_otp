#!/usr/bin/python3.9
from base64 import b32decode, b32encode

def	ft_base_64():
	s = b'Hola!'
	print(s)
	s = b32encode(s)
	print(s)

	deco = b32decode(s)
	print(deco)

ft_base_64()