from Nodo import Nodo
from Lista import Lista


if __name__ == "__main__":
	lis = Lista()	
	nombre = "Lo que sea"
	apellido = "La mona"
	nod = Nodo(nombre)
	nod2 = Nodo(apellido)
	lis.agregar(nod)
	lis.agregar(nod2)
	lis.listar()
