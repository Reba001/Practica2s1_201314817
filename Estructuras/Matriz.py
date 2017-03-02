from ListaDoble import ListaDoble
from Nodo import Nodo

class MatrizD : 
	def __init__(self):
		self.__nodoMDCabezaY = None
		self.__nodoMDColaY = None
		self.__nodoMDColaX = None
		self.__nodoMDCabezaY = None

		self.__X = ListaDoble()  #Representa columna (los dominios)
		self.__Y = ListaDoble() #Representa Fila (la inicial de cada nombre)
		self.__Z = ListaDoble()	#Representa Largo (todos los nombres en cada dominio) 
		self.__tamanioX = 0 # tamanio de la columna
		self.__tamanioY = 0	# tamanio de la fila
		self.__tamanioZ = 0 # tamanio del largo


	
	def setDatos(self, datoX, datoY, datoZ) :
		nodoDisperso = Nodo(datoZ)# nodo disperso que se hizo para guardar el nodo que ha de apuntar hacia arriba , abajo, siguiente y anterior 
		
		
		if self.__X.busquedaPorDato(datoX) != True:
			print "Dato no se encuentra dentro de la matriz"
			self.__X.setOrdenado(datoX)
		
		if self.__Y.busquedaPorDato(datoY) != True:
			print "Dato ya se encuentra dentro de la matriz"
			self.__Y.setOrdenado(datoY)
		
		if self.__Y.busquedaPorDato(datoY) == True : # busqueda de la primer letra del nombre del correo
			nodoCY = self.__Y.busquedadeNodo(datoY)
			if nodoCY.pAb == None : 
				nodoCY.pAb = nodoDisperso
				nodoDisperso.pAnt = nodoCY
			else :
				nodoCabezaD = nodoCY.pAb
				nodoCabezaD.pSig = nodoDisperso
				nodoDisperso.pAnt = nodoCabezaD 

		

		if self.__X.busquedaPorDato(datoX) == True : 
			nodoCX = self.__X.getCabeza()





		
		









	def crearMatriz(self):# metodo para crear una matriz dispersa 
		
				

















