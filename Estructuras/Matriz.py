from ListaDoble import ListaDoble
from Nodo import Nodo

class MatrizD : 
	def __init__(self):
		self.__X = ListaDoble()  #Representa columna (los dominios)
		self.__Y = ListaDoble() #Representa Fila (la inicial de cada nombre)
		self.__Z = ListaDoble()	#Representa Largo (todos los nombres en cada dominio) 
		self.__tamanioX = 0 # tamanio de la columna
		self.__tamanioY = 0	# tamanio de la fila
		self.__tamanioZ = 0 # tamanio del largo


	
	def setDatos(self, datoX, datoY, datoZ) :

		if self.__X.getVacio() == True:
		 	self.__X.setNodoPrimero(datoX)
			self.__Y.setNodoPrimero(datoY)
			self.__Z.setNodoPrimero(datoZ)
		else :
			self.ordenarX(datoX)
			self.ordenarY(datoY)
			self.ordenarZ(datoZ)

	def ordenarX(self, datoX):


	def ordenarY(self, datoY):


	def ordenarZ(self, datoZ):
		











