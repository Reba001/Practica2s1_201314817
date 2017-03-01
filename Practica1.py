import sys
sys.path.append('./Estructuras')
from Lista import Lista
from ListaDoble import ListaDoble


if __name__ == "__main__":
	lis = Lista()	
	lsD = ListaDoble()
	nombre = "Lo que sea"
	print nombre[0], nombre[3]
	apellido = "a mona"
	cualquier = "Policia"
	lis.setNodoInicio(nombre)
	lis.setNodoInicio(apellido)
	lis.setNodoInicio(cualquier)
	lis.setNodoFinal(nombre)
	lis.imprimirListaCompleta()

	lsD.setOrdenado(nombre)
	lsD.setOrdenado(apellido)
	lsD.setOrdenado(cualquier)

	lsD.getLista()
