De que consta el pack.

configuracioAUTh
privoxy
screenlet
telecentreuser
Web
Webservice

ConfiguracioAUTH
------------------------

Dintre de la carpeta ja hiha una explicaci� de que s'ha de fer.
1er. Modificar el gdm perqu� no surtin la llista dels usuaris. (ja ho fa script d'instal�laci�) 
La carpeta /etc/pam.d son els arxius que s'han modificat perqu� en cas de que un usuari tingui password en blanc , automaticament entri, mitjan�ant GDM
La carpeta /etc/gdm s'han modificat perqu� a l'entrar l'usuari restaura la carpeta Home/$USER. llavors hia una altre modificacio que fa que quan 
l'usuari surti ho guarda en el Log, sigui usuari registrat per ID o no .
tambe dintre el Init executa un script /usr/share/local/telstany/users.py que afegeix els usuaris que s'han donat d'alta.

 
2on. Si no s'ha fet mai en el pc la sol�luci� mes senzilla es copiar app Gnome-appearance-properties.desktop dintre de /usr/sharegdm/autostart/LoginWindow
ja que quan s'inici el GDM et demanar� quin tema vols posar. ( Copiant les carpetes que copia script d'instal�laci� ) ja queda canviat.



Privoxy
-----------------------
L'ordinador s'ha d'haver instal�lat el paquest privoxy
LLavors s'executa l'script que es baixa les llistes de Shallalist.de .
Llavors s'hauria de modificar l'usuari que ens interessi que utilizi el privoxy.
Per defecte si hem copiat el telecentreuser -> ja porta la configuracio del privoxy .


screenlet 
---------------------
Aqui hiha l'screenlet per instal�lar.
En el telecentreuser ja est� copiat.


telecentreuser
------------------------
S'ha de crear pr�viament usuari telecentreuser
�s la carpeta que s'ha de copiar a /etc/telestany perqu� el GDM cada vegada que entres la copia en el Home aixi tenim una carpeta arreglada

Web
----------------------
P�gina amb php de la Gesti� d'usuaris 

WebService
----------------------
WEb service fet amb python que serveix perqu� funcioni screenlet i la creacio d'usuaris
El webservice en funcio de la IP del servidor s'ha de canviar la IP en el programa webservice.py


Executar installClient.sh i fa instal�lacio en el PC del Client -> Privoxy , ConfiguracioAuth, telecentre User
Execuer installServer.sh i fa instal�lacio per a servidor -> Web i WebService

En el client hiha d'haver-hi els seg�ents paquests: sshd, gxmessage, Pytoh Soappy screenlets,python-utils
