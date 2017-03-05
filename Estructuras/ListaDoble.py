import Nodo
n = Nodo
nodoVacio = Nodo
class ListaDoble(object):
	def __init__(self):
		
		self.__cabeza = None
		self.__cola = None
		self.__tamanio = 0

	def getCabeza (self):
		return self.__cabeza

	def getCola(self) : 
		return self.__cola	

	def setCabeza(self, cabeza):
		self.__cabeza = cabeza

	def setCola(self, cola):
		self.__cola	= cola

	def getVacio(self):
		if self.__cabeza == None :
			return True
		else : 
			return False
	


	def setNodoPrimero(self, dato):
		nv = nodoVacio.Nodo("")
		nuevo = n.Nodo(dato)
		nuevo.pAb = nv 
		nuevo.pArr = nv
		if self.getVacio() == True:
			self.__cabeza = self.__cola = nuevo

		else : 
			nuevo.pSig = self.__cabeza
			self.__cabeza.pAnt = nuevo
			self.__cabeza = nuevo

		self.__tamanio += 1 #tamanio de la lista 

	def setNodoUltimo(self,dato):
		nv = nodoVacio.Nodo("")
		nuevo = n.Nodo(dato)
		nuevo.pAb = nv
		nuevo.pArr = nv
		if self.getVacio() == True : 
			self.__cabeza = self.__cola = nuevo
		else:
			self.__cola.pSig = nuevo
			nuevo.pAnt = self.__cola
			self.__cola = nuevo


		self.__tamanio += 1

	def getLista(self):
		if self.getVacio() == True :
			print "Lista Vacia no se porque entra de ultimo"
		else : 
			#print "------------------------------"
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
		nv = nodoVacio.Nodo("")
		nuevo = n.Nodo(dato)
		nuevo.pArr = nv
		nuevo.pAb = nv
		if self.getVacio() == True : 
			self.__cabeza = self.__cola = nuevo 
			self.__cola.pSig = nv
			self.__tamanio += 1	
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
				else:
					nodoanterior = aux.pAnt
					nodoanterior.pSig = nuevo
					nuevo.pAnt = nodoanterior
					nuevo.pSig = aux
					aux.pAnt = nuevo
					self.__tamanio += 1


	
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

	def buscarPorPosicion(self,posicion):
		temp = self.__cabeza
		if self.getVacio() == True : 
			print "Imposible eliminar esta vacio"
		
		else :
			validar = True
			contador = 0
			
			if posicion > 0 :
				while validar :
					if posicion == contador:
						validar = False
						break
					
					if temp == self.__cola:
						validar = False
					else:
						contador += 1
						temp = temp.pSig
		return temp
			


	def busquedaPorDato(self, dato):
		encontrado = False
		if self.getVacio() == True :
			print "oie si que rukistrukis"
		else : 
			#print "------------------------------"
			validar = True 
			temp = self.__cabeza
			while (validar) : 
				if temp.getElemento() == dato : 
					validar = False
			#		print temp.getElemento()
					encontrado = True 
				if temp == self.__cola : 
					validar = False 
				else : 
					temp = temp.pSig
		return encontrado

		

	def busquedadeNodo(self, dato):
		temp = self.__cabeza
		if self.getVacio() == True :
			print "oie si que rukistrukis"
		else : 
			#print "------------------------------"
			
			while temp != None :

				if temp.getElemento() == dato :
				#	print "awebo nodo encontrado prro alv" , temp.getElemento()
				#	if temp != self.__cola :
				#		print "awebo nodo puntero siguiente", temp.pSig.getElemento()
				#	else: 
				#		print "llegaste al ultimo nodo prro"
					break

				temp = temp.pSig
		
		return temp










