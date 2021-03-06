#!/bin/python
# coding=utf-8

from PyZenity import ErrorMessage
from PyZenity import GetDirectory
from PyZenity import InfoMessage
from PyZenity import Notification
from PyZenity import GetFilename


#GetFilename
def get_archivo():
	print("#Get archivo:")
	archivo=None
	try:
		archivo = GetFilename(multiple=True,sep='|')
		print("Tipo: ",type(archivo))
		InfoMessage('Archivo seleccionado:' +str(archivo),width=200,height=150,title='Archivo seleccionado')
	except Exception as ex:
		ErrorMessage('Ha ocurrido una excepcion: '+str(ex))
	finally:
		print("Ha finalizado el bloque: ")
		print("Archivo: ",str(archivo))


#GetDirectory
def get_directorio():
	print("#Get directorio:")
	directorio = None
	try:
		directorio = GetDirectory(multiple=False,selected=None,sep=None)
		InfoMessage('Tu selección es: '+str(directorio),width=200,height=150,title='Directorio seleccionado')
		Notification(text='Tu selección es: '+str(directorio))
	except Exception as ex:
		ErrorMessage('Ha ocurrido una excepcion: '+str(ex))
	finally:
		print("Ha finalizado el bloque:")
		print("Directorio: ",str(directorio))


def main():
	#get_directorio()
	get_archivo()


if __name__ == '__main__':
    main()

