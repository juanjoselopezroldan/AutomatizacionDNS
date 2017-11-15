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
else:
        print " "
        print "Error, los parametros introducidos no son validos por favor siga la siguiente sintaxis: "
        print " "
        print "1º -> -a o -b, Si recibe -a añadirá un nuevo nombre en el DNS, si recibe -b borrará el no$
        print "2º -> -dir o -alias, si recibe -dir va a crear un registro tipo A, si recibe -alias va a $
        print "3º -> El nombre de la máquina para añadir o borrar"
        print "4º -> El nombre del alias o la dirección ip: Si has usuado la opción -dir recibirá una ip$
        print " "
        print "-Ejemplo de sintaxis: "
        print "    Añadir: python script.py -a -dir smtp 172.22.200.200"
        print "    Eliminar:  python script.py -b smtp"
        print " "
        exit()

print "Cambios realizados satisfactoriamente"
os.system('systemctl restart bind9')