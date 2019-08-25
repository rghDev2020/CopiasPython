#!/bin/python
# coding=utf-8

from PyZenity import InfoMessage
from PyZenity import ErrorMessage


MENSAJE = "Bienvenido a Python for Beginners."

def get_mensaje():
	global MENSAJE
	InfoMessage(MENSAJE, width=250,height=140,title="Python for Beginners")


def get_error(dato):
	if dato == None:
		ErrorMessage("Ha ocurrido un error, pero lo corregiremos pronto.",width=250,height=140,title="Python for Beginners")
	else:
		InfoMessage("Dato de entrada: "+dato,title="Hola y adios");
