from ListaDoble import ListaDoble
from Nodo import Nodo

class MatrizD(object) : 
	def __init__(self):
		self.__nodoDisperso = None
		self.__contZ = 0
		self.__X = ListaDoble()  #Representa columna (los dominios)
		self.__Y = ListaDoble() #Representa Fila (la inicial de cada nombre)
		self.__Z = ListaDoble()	#Representa Largo (todos los nombres en cada dominio) 
		self.__tamanioX = 0 # tamanio de la columna
		self.__tamanioY = 0	# tamanio de la fila
		self.__tamanioZ = 0 # tamanio del largo


	
	def setDatosY(self, datoY) :
		if self.__Y.busquedaPorDato(datoY) == False :
			self.__Y.setOrdenado(datoY)

		self.__Y.getLista()


	def setDatosZ(self, datoZ, datoX):
		nodoDisperso = Nodo(datoZ)# nodo disperso que se hizo para guardar el nodo que ha de apuntar hacia arriba , abajo, siguiente y anterior
		if self.__X.busquedaPorDato(datoX) == False :
			self.__X.setOrdenado(datoX)# sino se encuentra en nuestra lista lo insgresamos 
		# buscamos el nodo qeu contiene nuestro nuevo dato ingresado
		nodoCX = self.__X.busquedadeNodo(datoX)
		

		self.__X.getLista()


		nodoDisperso = Nodo(datoZ)# nodo disperso que se hizo para guardar el nodo que ha de apuntar hacia arriba , abajo, siguiente y anterior
		if self.__Y.busquedaPorDato(datoZ[0]) == True : # busqueda de la primer letra del nombre del correo
			print "Encontrado ni me preguntes we que dato es :v alv prro"
			nodoCY = nodoColaY = self.__Y.busquedadeNodo(datoZ[0])
			print "awebo prro es un error arreglado prro", nodoCY.getElemento()

			if nodoCY.pAb.getElemento() == "" :
				print "por fin prro resolviste el problema de asignacion de memoria"
				nodoCY.pAb = None
				nodoCY.pAb = nodoDisperso
				nodoDisperso.pArr = nodoCY
				print "Primer Dato Fila hacia abajo" , nodoCY.pAb.getElemento()

		if nodoCX.pAb.getElemento() == "" :
			nodoCX.pAb = None
			nodoCX.pAb = nodoDisperso
			nodoDisperso.pArr = nodoCX
			print "primer Dato de columna hacia abajo" , nodoCX.pAb.getElemento()

		

	
	def busquedaColaFila(self, cabeza):
		temp = cabeza
		if cabeza == None : 
			print "Fila vacia"
		else : 
			print "-------------------------"
			validar = True
			 
			while (validar):
				if temp == None:
					validar = False
				else : 
					temp = temp.pAb
		return temp

	def imprimirFila(self, cabeza):
		if cabeza == None : 
			print "Fila vacia"
		else : 
			print "-------------------------"
			validar = True
			temp = cabeza 
			cola = self.busquedaColaFila(cabeza)
			while (validar):
				print temp.getElemento()
				if temp == cola:
					validar = False
				else : 
					temp = temp.pSig






		
		






















