class Nodo(object):
	def __init__(self, elemento):
		#Atributo que tendra el elemento
		self.__elemento = elemento
		#puntero que servira para "unir a los dos nodos"
		#cuando se construya la lista
		self.__pSig = None
		self.__pAnt = None
		self.__pAb = None
		self.__pArr = None
 

	def getElemento(self):
		return self.__elemento



