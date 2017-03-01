import sys
sys.path.append('./Estructuras')
from Lista import Lista
from ListaDoble import ListaDoble


if __name__ == "__main__":
	lis = Lista()	
	lsD = ListaDoble()
	nombre = "lo que sea"
	print nombre[0], nombre[3]
	apellido = "a mona"
	cualquier = "policia"
	lis.setNodoInicio(nombre)
	lis.setNodoInicio(apellido)
	lis.setNodoInicio(cualquier)
	lis.setNodoFinal(nombre)
	lis.imprimirListaCompleta()

	for c in cualquier:
		print c

	lsD.setOrdenado(nombre)
	lsD.setOrdenado(apellido)
	lsD.setOrdenado('almolonga')
	lsD.setOrdenado(cualquier)
	lsD.setOrdenado('banana')
	lsD.setOrdenado('calzado')
	lsD.setOrdenado('baboso')
	lsD.setOrdenado('siseperonowadecir')
	lsD.setOrdenado('sister')
	lsD.setOrdenado('buey')
	lsD.setOrdenado('nose')
	lsD.setOrdenado('candido')
	

	lsD.getLista()
