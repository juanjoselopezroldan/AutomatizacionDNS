# AutomatizacionDNS
Script realizado en python que permite realizar la introducion de registros NS o CNAME en un DNS Bind9

Los parametros que tendremos que indicarle al script es el siguiente:

* ``-a`` o ``-b``: Si recibe ``-a`` añadirá un nuevo nombre, si recibe ``-b`` borrará el nombre que ha recibido.
* ``-dir`` o ``-alias``, si recibe ``-dir`` va a crear un registro tipo A, si recibe ``-alias`` va a crear un registro CNAME
* El nombre de la máquina para añadir o borrar
* El nombre del alias o la dirección ip: Si has usuado la opción ``-dir`` recibirá una ip y si has usuado ``-alias`` recibirá el nombre de la máquina a la que le vamos a hacer el alias. Si has utilizado -b no teendrá este parámetro.
