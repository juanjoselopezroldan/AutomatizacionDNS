#-*-coding: utf-8 -*-
import sys,os
opcion1=sys.argv[1]
tipo=sys.argv[2]
nombre=sys.argv[3]
dato=sys.argv[4]

if opcion1 == '-a':
	listad = open('/var/cache/bind/db.lopez.gonzalonazareno.org', 'a')
	listai = open('/var/cache/bind/db.172.22.200', 'a')

	if tipo == 'dir':
		listad.write(nombre+'	IN	A	'+dato+'\n')
		listai.write(dato+'	IN	PTR	'+nombre+'.lopez.gonzalonazareno.org.\n')
	

