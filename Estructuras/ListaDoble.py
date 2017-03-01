import Nodo
n = Nodo

class ListaDoble(object):
	def __init__(self):
		self.__cabeza = None
		self.__cola = None
		self.__tamanio = 0

	def getCabeza (self):
		return self.__cabeza

	def getCola(self) : 
		return self.__cola	

	def getVacio(self):
		if self.__cabeza == None :
			return True
		else : 
			return False


	def setNodoPrimero(self, dato):
		nuevo = n.Nodo(dato)
		if self.getVacio() == True:
			self.__cabeza = self.__cola = nuevo
		else : 
			nuevo.pSig = self.__cabeza
			self.__cabeza.pAnt = nuevo
			self.__cabeza = nuevo

		self.__tamanio += 1 #tamanio de la lista 

	def setNodoUltimo(self,dato):
		nuevo = n.Nodo(dato)
		if self.getVacio() == True : 
			self.__cabeza = self.__cola = nuevo
		else:
			self.__cola.pSig = nuevo
			nuevo.pAnt = self.__cola
			self.__cola = nuevo

		self.__tamanio += 1

	def getLista(self):
		if self.getVacio() == True :
			print "Lista Vacia"
		else : 
			print "------------------------------"
			validar = True 
			temp = self.__cabeza
			while (validar) : 
				print (temp.getElemento())
				if temp == self.__cola : 
					validar = False 
				else : 
					temp = temp.pSig

	def eliminarPrimero(self):
		if self.getVacio() == True : 
			print "Imposible eliminar lista vacia"
		elif self.__cabeza == self.__cola : 
			self.__cabeza = None
			self.__cola = None
			print "Elemento Eliminado de la Lista"
		else : 
			self.__cabeza = self.__cabeza.pSig
			self.__cabeza.pAnt = None
		self.__tamanio -= 1


	def eliminarUltimo(self):
		if self.getVacio() == True :
			print "Imposible Eliminar lista vacia"
		elif self.__cabeza == self.__cola : 
			self.__cabeza = None
			self.__cola = None
			print "Ultimo elemento eliminado de la lista"
		else : 
			self.__cola = self.__cola.pAnt
			self.__cola.pSig = None
		self.__tamanio -= 1
	
	def setOrdenado(self, dato):
		nuevo = n.Nodo(dato)
		if self.getVacio() == True : 
			self.__cabeza = self.__cola = nuevo	
		else : 
			aux = self.__cabeza
			c = ord(dato[0])
			validar = True
			i = 0

			while aux != self.__cola and ord(aux.getElemento()[i]) < c :
				aux = aux.pSig

			if aux == self.__cola and ord(aux.getElemento()[i]) < c :
				self.setNodoUltimo(dato)
			else :
				if aux == self.__cabeza:
					self.setNodoPrimero(dato)
				elif ord(aux.getElemento()[i]) == c :
					print "hola el elemento es igual :v"
					for caracter in dato:
						if caracter != aux.getElemento()[i]:
							c = ord(caracter)
							break
						else:
							i += 1

					if aux == self.__cola and ord(aux.getElemento()[i]) < c:
						self.setNodoUltimo(dato)
					else : 
						if aux == self.__cabeza:
							self.setNodoPrimero(dato)

					#if  ord(aux.getElemento()[i]) < c :
					#	nodosiguiente = aux.pSig
					#	nodosiguiente.pAnt = nuevo
					#	nuevo.pSig = nodosiguiente
					#	nuevo.pAnt = aux
					#	aux.pSig = nuevo
						else:

							nodoanterior = aux.pAnt
							nodoanterior.pSig = nuevo
							nuevo.pAnt = nodoanterior
							nuevo.pSig = aux
							aux.pAnt = nuevo						
				else:
					nodoanterior = aux.pAnt
					nodoanterior.pSig = nuevo
					nuevo.pAnt = nodoanterior
					nuevo.pSig = aux
					aux.pAnt = nuevo

	
	def getTamanio(self):
		return self.__tamanio

	def eliminarPorPosicion(self, posicion):
		if self.getVacio() == True : 
			print "Imposible eliminar esta vacio"
		else :
			if posicion == 0 :
				self.eliminarPrimero()
			elif posicion == (self.__tamanio-1) :
				self.eliminarUltimo()
			else:

				nodoactual = self.__cabeza
				nodoanterior= self.__cabeza
				k=0
				if posicion > 0 :
					while k != posicion and nodoactual.pSig != None :
						nodoanterior = nodoactual
						nodoactual = nodoactual.pSig
						k += 1
					if k == posicion :
						nodotemporal = nodoactual.pSig
						nodoanterior.pSig = nodoactual.pSig
						nodotemporal.pAnt = nodoanterior
			self.__tamanio -= 1
				 










