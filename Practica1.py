import sys
sys.path.append('./Estructuras')
from Lista import Lista
from ListaDoble import ListaDoble


if __name__ == "__main__":
	lis = Lista()	
	lsD = ListaDoble()
	nombre = "Lo que sea"
	print nombre[0], nombre[3]
	apellido = "La mona"
	cualquier = "Policia"
	lis.setNodoInicio(nombre)
	lis.setNodoInicio(apellido)
	lis.setNodoInicio(cualquier)
	lis.setNodoFinal(nombre)
	lis.imprimirListaCompleta()
	print lis.getNodoPrimero().getElemento()
	print lis.getNodoUltimo().getElemento()

	lsD.setNodoPrimero(nombre)
	lsD.setNodoPrimero(apellido)
	lsD.setNodoPrimero(cualquier)

	lsD.getLista()
	print lsD.getTamanio()
	lsD.eliminarPorPosicion(2)

	lsD.getLista()