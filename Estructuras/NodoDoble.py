class NodoDoble(object):
	def __init__ (self, elemento):
		self.elemento = elemento
		self.sig = None
		self.ant = None

	def getElemento(self):
		return self.elemento
