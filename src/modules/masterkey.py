import shelve, os
import modules.utils.stdmsg as msg
global default_keypath
default_keypath = "/home/modules/key/ft_opt.key"

class MasterKey:
	def __init__(self, k = "", keypath = default_keypath):
		self._key = k
		self._keypath = keypath

	def set_key(self, k):
		self._key = k

	def get_key(self):
		return self._key
	
	def get_keypath(self):
		return self._keypath
	
	def set_keypath(self, k):
		self._keypath = k

	def ConfirmCreateNewKey():
		if os.path.exists(default_keypath):
			msg.warn_msg("Another key exist. This action will overwrite it and is irreversible. Are you sure you want to overwrite it? [y/n] : ")
			usrInput = str(input(""))
			if usrInput == 'n' or usrInput == 'N':
				print("cancel key-gen and return program")
				return False
			elif usrInput == 'y' or usrInput == 'Y':
				return True
			else:
				msg.err_msg("Please write 'y' or 'n'")
				MasterKey.ConfirmCreateNewKey()
		return True

#	@property
#	def key(self):
#		return self._key
	
#	@key.setter
#	def key(self, k):
#		self._key = k

#	@key.deleter
#	def key(self):
#		del self._key

#	@property
#	def keypath(self):
#		return self._keypath
	
#	@keypath.setter
#	def keypath(self, k):
#		self._keypath = k

#	@keypath.deleter
#	def keypath(self):
#		del self._keypath

def PersistKey(mykey):
	database = shelve.open('key/database')
	k = mykey
	database['key'] = k