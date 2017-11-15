#-*-coding: utf-8 -*-
import sys,os
opcion1=sys.argv[1]
tipo=sys.argv[2]
if opcion1 == '-a':
	listad = open('/var/cache/bind/db.lopez.gonzalonazareno.org', 'a')
	listai = open('/var/cache/bind/db.172.22.200', 'a')
	nombre=sys.argv[3]
	dato=sys.argv[4]
	if tipo == '-dir':
		listad.write(nombre+'	IN	A	'+dato+'\n')
		listai.write(dato+'	IN	PTR	'+nombre+'.lopez.gonzalonazareno.org.\n')
	elif tipo == '-alias':
		listad.write(nombre+'	IN	CNAME	'+dato+'.lopez.gonzalonazareno.org.\n')
	listad.close()
	listai.close()
elif opcion1 == '-b':
	os.system('sed -i /'+tipo+'/d /var/cache/bind/db.lopez.gonzalonazareno.org')
	os.system('sed -i /'+tipo+'/d /var/cache/bind/db.172.22.200')
os.system('systemctl restart bind9')