from ListaDoble import ListaDoble
from Nodo import Nodo
nodoVacio = Nodo

class MatrizD(object) : 
	def __init__(self):
		self.__X = ListaDoble()  #Representa columna (los dominios)
		self.__Y = ListaDoble() #Representa Fila (la inicial de cada nombre)
		self.__Z = ListaDoble()	#Representa Largo (todos los nombres en cada dominio) 
		self.__tamanioX = 0 # tamanio de la columna
		self.__tamanioY = 0	# tamanio de la fila
		self.__tamanioZ = 0 # tamanio del largo


	
	#def setDatosY(self, datoY) :
		

		#self.__Y.getLista()


	def setDatosZ(self, datoZ, datoX):
		#nv = nodoVacio.Nodo("")
		
		insercion = True
		nodoDisperso = Nodo(datoZ)# nodo disperso que se hizo para guardar el nodo que ha de apuntar hacia arriba , abajo, siguiente y anterior
		#nodoDisperso.pSig = nodoVacio.Nodo("")
		#nodoDisperso.pAnt = nodoVacio.Nodo("")
		if self.__Y.busquedaPorDato(datoZ[0]) == False :
			self.__Y.setOrdenado(datoZ[0])
		
		if self.__X.busquedaPorDato(datoX) == False :
			self.__X.setOrdenado(datoX)# sino se encuentra en nuestra lista lo insgresamos 

		# buscamos el nodo qeu contiene nuestro nuevo dato ingresado
		 
		nodoCX =  self.__X.busquedadeNodo(datoX)
		

		#self.__X.getLista()


		#if self.__Y.busquedaPorDato(datoZ[0]) == True : # busqueda de la primer letra del nombre del correo
		#print "Encontrado ni me preguntes we que dato es :v alv prro"
		nodoCY =  self.__Y.busquedadeNodo(datoZ[0])

		#print "awebo prro es un error arreglado prro", nodoCY.getElemento()
		if nodoCX.pAb.getElemento() == "" :#concatena primeros datos con columna
			
			nodoCX.pAb = None
			nodoCX.pAb = nodoDisperso
			nodoDisperso.pAnt = None
			nodoDisperso.pAnt = nodoCX
			nodoCX.setTamanioFila(2)


			
			#print "primer Dato de columna hacia abajo" , nodoCX.pAb.getElemento()
		else :
			if self.encontrarenColumna(nodoCX, datoZ) == True :
				nodoProfundidad = self.buscarenColumna(nodoCX, datoZ)
				if nodoProfundidad.getTamanioFila() == 0 :

					print "por fin encontrado", datoZ
					insercion = False
					print "por fin esta es la cabeza: " , nodoProfundidad.getElemento()
					nodoProfundidad.pAtr = nodoDisperso
					nodoDisperso.pAde = nodoProfundidad
					nodoProfundidad.setTamanioFila(2)

					print "aniadido atras", nodoProfundidad.pAtr.getElemento()
					self.imprimirProfundidad(nodoProfundidad)
					print "tamanio profundiad", nodoProfundidad.getTamanioFila()
				else :
					print "por fin esta es la cabeza: " , nodoProfundidad.getElemento()
					temp = nodoProfundidad
					contador = 0
					vale = True 
					while vale : 
						if contador == (nodoProfundidad.getTamanioFila()-1):
							vale = False
						else:
							contador += 1
				 			temp = temp.pAtr

			#	print "Entrada: " , datoZ
			#	print "Cola final fila: ", temp.getElemento()
					temp.pAtr = nodoDisperso
					nodoDisperso.pAde = temp
					nodoProfundidad.setTamanioFila(nodoProfundidad.getTamanioFila() + 1)

					self.imprimirProfundidad(nodoProfundidad)
					print "tamanio profundiad", nodoProfundidad.getTamanioFila()
					insercion = False


			else:

			#if insercion == True :

			#	print "este era el error"
				temp = nodoCX.pAb
				c = ord(datoZ[0])
				contador = 1
		
				while contador != (nodoCX.getTamanioFila()-1) and ord(temp.getElemento()[0]) < c:
					temp = temp.pSig
					contador += 1

				if contador == (nodoCX.getTamanioFila()-1) and ord(temp.getElemento()[0]) < c:
					temp.pSig  = nodoDisperso
					nodoDisperso.pAnt = temp
				else:
					if temp == nodoCX.pAb :
						nodoDisperso.pSig = temp
						temp.pAnt = nodoDisperso
						nodoDisperso.pAnt = nodoCX
						nodoCX.pAb = nodoDisperso
					else : 
						nodoanterior = temp.pAnt
						nodoanterior.pSig = nodoDisperso
						nodoDisperso.pAnt = nodoanterior
						nodoDisperso.pSig = temp
						temp.pAnt = nodoDisperso
					#	print "Entrada: " , datoZ
				nodoCX.setTamanioFila(nodoCX.getTamanioFila() + 1)
			#print "Tamanio de la columna: ", str(nodoCX.getTamanioFila())

		if nodoCY.pAb.getElemento() == "" :# concatena primeros datos con fila
		#	print "por fin prro resolviste el problema de asignacion de memoria"
			nodoCY.pAb = None
			nodoCY.pAb = nodoDisperso
			nodoDisperso.pArr = None
			nodoDisperso.pArr = nodoCY
			nodoCY.setTamanioFila(2)
				
			#print "Primer Dato Fila hacia abajo" , nodoCY.pAb.getElemento()
		else :
			if insercion == True:
				temp2 = nodoCY.pAb
				temp = self.__X.getCabeza()
				c = ord(datoX[0])
				contador = 1
		
				while contador != (nodoCY.getTamanioFila() - 1) and ord(temp.getElemento()[0]) < c:
					temp = temp.pSig
					temp2 = temp2.pAb
					contador += 1
					

				if contador == (nodoCY.getTamanioFila() - 1) and ord(temp.getElemento()[0]) < c:
					temp2.pAb  = nodoDisperso
					nodoDisperso.pArr = temp2
				else:
					if temp2 == nodoCY.pAb :
						nodoDisperso.pAb = temp2
						temp2.pArr = nodoDisperso
						nodoDisperso.pArr = nodoCY
						nodoCY.pAb = nodoDisperso
					else : 
						nodoanterior = temp2.pArr
						nodoanterior.pAb = nodoDisperso
						nodoDisperso.pArr = nodoanterior
						nodoDisperso.pAb = temp2
						temp2.pArr = nodoDisperso
					#	print "Entrada: " , datoZ
				nodoCY.setTamanioFila(nodoCY.getTamanioFila() + 1)
			#	print "Entrada: " , datoZ
			#	print "Cola final fila: ", temp.getElemento()
				#temp.pAb = nodoDisperso
				#nodoDisperso.pArr = temp
				#nodoCY.setTamanioFila(nodoCY.getTamanioFila() + 1)
					

			#	print "Tamanio de la fila: ", str(nodoCY.getTamanioFila())

		
	def eliminarCorreo(self, datoX, datoZ):
		if self.__X.getVacio() == True:
			print "vacia"
		else : 
			tempY = self.__Y.busquedadeNodo(datoZ[0])
			tempX = self.__X.busquedadeNodo(datoX)
			print "tamanio: " , tempX.getTamanioFila()
			nodoActual = self.buscarenColumna(tempX, datoZ)
			if nodoActual.getTamanioFila() == 0 :
				nodoArr = nodoActual.pArr
				nodoAb = nodoActual.pAb
				nodoSig = nodoActual.pSig
				nodoAnt = nodoActual.pAnt
				nodoArr.pAb = nodoAb
				nodoAb.pArr	= nodoArr
				nodoSig.pAnt = nodoAnt
				nodoAnt.pSig = nodoSig
				nodoActual = None
			else:
				validar = True
				contador = 0 
			#	temp = nodoActual 
				while (validar) : 
					if nodoActual.getElemento() == datoZ:
						print "puntero Arriba: ", nodoActual.pArr.getElemento()
						print "Elemento a eliminar: " , nodoActual.getElemento()
						print "puntero atras: " , nodoActual.pAtr.getElemento() 

						validar = False 
						break	

					if contador == (nodoActual.getTamanioFila()-1):
						validar = False
					else :
						contador += 1
						nodoActual = nodoActual.pAtr

				if contador == 0 :
					nodoAnt = nodoActual.pAnt
					nodoActual.pAtr.pAnt = nodoAnt
					nodoAnt.pSig = nodoActual.pAtr
					print "puntero anterior", nodoActual.pAtr.pAnt.getElemento()
					print "puntero siguiente de anterior" , nodoAnt.pSig.getElemento()
					nodoSig = nodoActual.pSig
					nodoActual.pAtr.pSig = nodoSig
					nodoSig.pAnt = nodoActual.pAtr
					print "puntero siguiente", nodoActual.pAtr.pSig.getElemento()
					print "puntero anterior de siguiente" , nodoSig.pAnt.getElemento()					
					nodoArr = nodoActual.pArr
					nodoActual.pAtr.pArr = nodoArr
					nodoArr.pAb = nodoActual.pAtr
					print "puntero arriba", nodoActual.pAtr.pArr.getElemento()
					print "puntero abajo de arriba" , nodoArr.pAb.getElemento()
					nodoAb = nodoActual.pAb
					nodoActual.pAtr.pAb =nodoAb
					nodoAb.pArr = nodoActual.pAtr
					print "puntero abajo", nodoActual.pAtr.pAb.getElemento()
					print "puntero arriba de abajo" , nodoAb.pArr.getElemento()
					nodoActual = nodoActual.pAtr


			tempY.setTamanioFila(tempY.getTamanioFila() - 1)
			tempX.setTamanioFila(tempX.getTamanioFila() - 1)
			print "tamanio despues de eliminar: " , tempX.getTamanioFila()
			print "encontre datoX: ", tempX.getElemento()
				

	def imprimirMatrizX(self):
		print "--------------------Columna--------------------"
		if self.__X.getVacio() == True:
			print "vacia"
		else : 
			validar = True
			tempX = self.__X.getCabeza()
			while (validar) :
				self.imprimirColumnas(tempX)
				if tempX == self.__X.getCola():
					validar = False
				else :
					tempX = tempX.pSig
		print "----------------End Columna---------------------"




	def imprimirMatrizY(self):
		print "--------------Fila-----------------"
		if self.__Y.getVacio() == True:
			print "vacia"
		else : 
			validar = True
			tempY = self.__Y.getCabeza()
			while (validar) :
				self.imprimirFila(tempY)

				if tempY == self.__Y.getCola():
					validar = False
				else : 
					tempY = tempY.pSig
		print "----------------End Fila ----------------"
	

	
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

	def imprimirColumnas (self, cabeza):
		if cabeza == None:
			print "Columna vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0
			temp = cabeza 
			while (validar):
				print temp.getElemento()
				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				elif contador == 0 : 
					contador +=1
					temp = temp.pAb
				else : 
					contador +=1
					temp = temp.pSig

 
	def imprimirProfundidad(self, cabeza):
		if cabeza == None:
			print "Fila vacia"
		else : 
			print "------------------------"
			validar = True
			contador = 0 
			temp = cabeza 
			while (validar) : 
				print "profundidad" ,temp.getElemento()
				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				else :
					contador += 1
					temp = temp.pAtr


	
	def imprimirFila(self, cabeza):
		if cabeza == None : 
			print "Fila vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0
			temp = cabeza 
			print "tamanio cuado se imprime: ", cabeza.getTamanioFila()
			while (validar):
				print temp.getElemento()
				if contador == (cabeza.getTamanioFila()-1):
					validar = False
					
				else : 
					contador +=1
					temp = temp.pAb

		#def buscarenColumnaEliminacion(self, cabeza, dato):
		#temp = cabeza
		#if cabeza == None:
		#	print "Columna vacia"
		#else : 
		#	print "-------------------------"
		#	validar = True
		#	contador = 0
		#	 
		#	while (validar):
		#		if dato == temp.getElemento():
		#			validar = False
		#			print temp.getElemento()
		#			break
#
#				if contador == (cabeza.getTamanioFila()-1):
#					validar = False
#				elif contador == 0 : 
#					contador +=1
#					temp = temp.pAb
#				else : 
#					contador +=1
#					temp = temp.pSig
#		return temp


	def buscarenColumna(self, cabeza, dato):
		temp = cabeza
		if cabeza == None:
			print "Columna vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0
			 
			while (validar):
				if dato[0] == temp.getElemento()[0]:
					validar = False
					print temp.getElemento()
					break

				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				elif contador == 0 : 
					contador +=1
					temp = temp.pAb
				else : 
					contador +=1
					temp = temp.pSig
		return temp




	def buscarenFila(self, cabeza, dato):
		temp = cabeza
		if cabeza == None : 
			print "Columna vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0

		 	while (validar):
				print temp.getElemento()
				if temp.getElemento() == dato:
					validar = False
					print temp.getElemento()
				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				else : 
					contador +=1
					temp = temp.pAb
		return temp


	def encontrarenFila(self, cabeza, dato):
		self.__tamanioX = -1
		encontrar = False
		if cabeza == None : 
			print "Columna vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0
			temp = cabeza
		 	while (validar):
				print temp.getElemento()
				if temp.getElemento() == dato:
					self.__tamanioX = contador
					validar = False
					encontrar = True
					print temp.getElemento()
				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				else : 
					contador +=1
					temp = temp.pAb
		return encontrar


	def encontrarenColumna(self, cabeza, dato):
		encontrar = False	
		if cabeza == None:
			print "Columna vacia"
		else : 
			print "-------------------------"
			validar = True
			contador = 0
			temp = cabeza	 
			while (validar):
				if dato[0] == temp.getElemento()[0]:
					validar = False
					encontrar = True
					print temp.getElemento()

				if contador == (cabeza.getTamanioFila()-1):
					validar = False
				elif contador == 0 : 
					contador +=1
					temp = temp.pAb
				else : 
					contador +=1
					temp = temp.pSig
		return encontrar







	








		
		






















