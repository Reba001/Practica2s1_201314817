import sys
sys.path.append('./Estructuras')
from Lista import Lista
from ListaDoble import ListaDoble
from Matriz import MatrizD


if __name__ == "__main__":
	lis = Lista()	
	lsD = ListaDoble()
	matriz = MatrizD()

	



	matriz.setDatosZ('almolonga', 'yahoo')
	matriz.setDatosZ('banamex', 'gmail')
	matriz.setDatosZ('omar', 'hotmail')
	matriz.setDatosZ('manha', 'outlook')
	matriz.setDatosZ('apari', 'gmail')
	matriz.setDatosZ('lara', 'gmail')
	matriz.setDatosZ('carmen', 'gmail')
	
	matriz.setDatosZ('anabanana', 'fiusac')

	matriz.setDatosZ('banana', 'yahoo')
	matriz.setDatosZ('oneii', 'yahoo')
	matriz.setDatosZ('manjar', 'yahoo')
	matriz.setDatosZ('mamaesta', 'yahoo')
	
	matriz.setDatosZ('lesli', 'yahoo')
	matriz.setDatosZ('carol', 'yahoo')
	matriz.setDatosZ('buenota', 'fiusac')
	matriz.setDatosZ('laila', 'gmail')
	matriz.setDatosZ('laruto', 'gmail')
	matriz.setDatosZ('mara', 'yahoo')
	matriz.setDatosZ('laila', 'fiusac')
	matriz.setDatosZ('maria', 'gmail')
	matriz.imprimirMatrizY()
	matriz.imprimirMatrizX()
	#print "aqui esta eliminando ..........."
	#matriz.eliminarCorreo('gmail' , 'banamex' )
	#matriz.eliminarCorreo('gmail', 'lara')
	#print "termino de eliminar ............"
	#matriz.imprimirMatrizY()
	#matriz.imprimirMatrizX()
	




	

