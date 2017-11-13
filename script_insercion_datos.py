#-*-coding: utf-8 -*-
import sys,commands

print "Bienvenido al script que te permite realizar la insercion de datos"

opcion1=str(raw_input("Introduce opcion -a (Añadirá nuevo registro) o -b (Eliminar registro): "))
if opcion1 == "-a":
	opcion2=str(raw_input("Introduce opcion -dir (Creará registro A) o -alias (Creará registro CNAME): "))

opcion3=str(raw_input("Introduce nombre maquina para añadir o borrar: "))

if opcion2 == "-dir":
	opcion4=str(raw_input("Introduce D. Ip: "))
else:
	opcion5=str(raw_input("Introduce N. Alias: "))
