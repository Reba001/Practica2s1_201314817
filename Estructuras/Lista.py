import Nodo
cn = Nodo

#Clase listaSimple

class Lista(object): 

	def __init__(self):

		self.__primero = None
		self.__ultimo = None
		self.__tamanio = 0


	def getVacio(self):
		if self.__primero == None:
			return True

	
	def setNodoInicio(self, elemento) :
		nuevo = cn.Nodo(elemento)
		if self.getVacio() == True:
			self.__primero = self.__ultimo = nuevo
		else : 
			nuevo.pSig = self.__primero
			self.__primero = nuevo
		self.__tamanio += 1


	def setNodoFinal(self, elemento) : 
		nuevo = cn.Nodo(elemento)
		if self.getVacio() == True :
			self.__primero = self.__ultimo = nuevo
		else : 
			self.__ultimo.pSig = nuevo
			self.__ultimo = nuevo
		self.__tamanio += 1

	def eliminarPrimero(self) : 
		if self.getVacio() == True : 
			print "Lista Vacia. Imposible eliminar  "
		elif self.__primero == self.__ultimo : 
			self.__primero = None
			self.__ultimo = None 
			print "Elemento eliminado la lista esta vacia "
		else : 
			temp = self.__primero
			self.__primero = self.__primero.pSig

		self.__tamanio -= 1	

	def eliminarUltimo(self) : 
		if self.getVacio()==True:
			print "Lista Vacia imposible eliminar"
		elif self.__primero == self.__ultimo :
			self.__primero = None
			self.__ultimo = None
			print "Elemento eliminado. La lista esta vacia"
		else:
			validar = True 
			temp = self.__primero 
			while (valida) :
				if temp.pSig == self.__ultimo:
					temp2 = self.__ultimo 
					self.__ultimo = temp
					temp2 = None
					validar = False 
					print "Elemento eliminado "
				else : 
					temp = temp.pSig
		self.__tamanio -= 1

	def getNodoPrimero(self) : 
		if self.getVacio() == True:
			return "Lista Vacia"
		else : 
			return self.__primero


	def getNodoUltimo(self):
		if self.getVacio() == True:
			return "Lista Vacia"
		else : 
			return self.__ultimo

	def eliminarPorPosicion(self, posicion):
		if self.getVacio() == True:
			print "Imposible eliminar la lista esta vacia"
		else:
			if posicion == 0 :
				self.eliminarPrimero()
			elif posicion == (self.__tamanio - 1) :
				self.eliminarUltimo()
			else:
				k = 0
				nodoactual = nodoanterior  = self.__primero
				while k != posicion and nodotemporal.pSig != None:
					nodoanterior = nodoactual
					nodoactual= nodoactual.pSig
					k += 1
				if k == posicion : 
					nodotemporal = nodoactual.pSig
					nodoanterior.pSig = nodotemporal.pSig
		self.__tamanio -= 1


	def imprimirListaCompleta(self) : 
		if self.getVacio() == True :
			print "Lista Vacia"
		else : 
			validar = True 
			temp = self.__primero
			while (validar) : 
				print (temp.getElemento())
				if temp == self.__ultimo : 
					validar = False 
				else : 
					temp = temp.pSig
