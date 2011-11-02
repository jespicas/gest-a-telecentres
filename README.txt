De que consta el pack.

configuracioAUTh
privoxy
screenlet
telecentreuser
Web
Webservice

ConfiguracioAUTH
------------------------

Dintre de la carpeta ja hiha una explicació de que s'ha de fer.
1er. Modificar el gdm perquè no surtin la llista dels usuaris. (ja ho fa script d'instal·lació) 
La carpeta /etc/pam.d son els arxius que s'han modificat perquè en cas de que un usuari tingui password en blanc , automaticament entri, mitjançant GDM
La carpeta /etc/gdm s'han modificat perquè a l'entrar l'usuari restaura la carpeta Home/$USER. llavors hia una altre modificacio que fa que quan 
l'usuari surti ho guarda en el Log, sigui usuari registrat per ID o no .
tambe dintre el Init executa un script /usr/share/local/telstany/users.py que afegeix els usuaris que s'han donat d'alta.

 
2on. Si no s'ha fet mai en el pc la sol·lució mes senzilla es copiar app Gnome-appearance-properties.desktop dintre de /usr/sharegdm/autostart/LoginWindow
ja que quan s'inici el GDM et demanarà quin tema vols posar. ( Copiant les carpetes que copia script d'instal·lació ) ja queda canviat.



Privoxy
-----------------------
L'ordinador s'ha d'haver instal·lat el paquest privoxy
LLavors s'executa l'script que es baixa les llistes de Shallalist.de .
Llavors s'hauria de modificar l'usuari que ens interessi que utilizi el privoxy.
Per defecte si hem copiat el telecentreuser -> ja porta la configuracio del privoxy .


screenlet 
---------------------
Aqui hiha l'screenlet per instal·lar.
En el telecentreuser ja està copiat.


telecentreuser
------------------------
S'ha de crear prèviament usuari telecentreuser
És la carpeta que s'ha de copiar a /etc/telestany perquè el GDM cada vegada que entres la copia en el Home aixi tenim una carpeta arreglada

Web
----------------------
Pàgina amb php de la Gestió d'usuaris 

WebService
----------------------
WEb service fet amb python que serveix perquè funcioni screenlet i la creacio d'usuaris
El webservice en funcio de la IP del servidor s'ha de canviar la IP en el programa webservice.py


Executar installClient.sh i fa instal·lacio en el PC del Client -> Privoxy , ConfiguracioAuth, telecentre User
Execuer installServer.sh i fa instal·lacio per a servidor -> Web i WebService

En el client hiha d'haver-hi els següents paquests: sshd, gxmessage, Pytoh Soappy screenlets,python-utils
