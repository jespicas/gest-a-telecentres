import SOAPpy
import sqlite3
import time
import os
import crypt,getpass,pwd
import urllib
import xml.sax
import xml.sax.handler

from datetime import datetime,date, timedelta
from SOAPpy import SOAPProxy
from time import gmtime, strftime
from xml.dom import minidom
from xml.dom.minidom import parseString

server = SOAPProxy('http://213.151.114.85:8082/')
usuaris = server.CrearUsuaris()
user = parseString(usuaris)
for usuari in user.getElementsByTagName("usuari"):
#    -p '"+crypt.crypt('',"SA")+"'
    value = "useradd -u "+usuari.attributes["id"].value+" -g users -G cdrom,floppy,audio,video,plugdev,lpadmin,dip,lp -s /bin/false -d /home/telecentreuser '"+usuari.attributes["nom"].value+"'"    
#    value = "userdel "+usuari.attributes["nom"].value
#    print value
    os.system(value)
    value = "passwd -d "+usuari.attributes["nom"].value
#   print value
    os.system(value)
    
usuaris = server.GetUsuarisEsborrar()
user= parseString(usuaris)
for usuari in user.getElementsByTagName("usuari"):
	value = "userdel "+usuari.attributes["nom"].value
	os.system(value)
	
