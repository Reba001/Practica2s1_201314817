class Nodo(object):
	def __init__(self, elemento):
		#Atributo que tendra el elemento
		self.__elemento = elemento
		self.__tamanioFila = 0
		#puntero que servira para "unir a los dos nodos"
		#cuando se construya la lista
		self.__pSig = None
		self.__pAnt = None
		self.__pAb = None
		self.__pArr = None
		self.__pAde = None
		self.__pAtr = None
 
	def actualizarElemento(self, elemento) : 
		self.__elemento = elemento

	def getElemento(self):
		return self.__elemento


	def setTamanioFila(self , tamanioFila):
		self.__tamanioFila = tamanioFila

	def getTamanioFila(self):
		return self.__tamanioFila



