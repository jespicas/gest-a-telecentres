import SOAPpy
import time
import logging
import urllib
import os
import sys
import xml.sax
import xml.sax.handler
from datetime import datetime,date, timedelta
from time import gmtime, strftime
from SOAPpy import SOAPProxy
from xml.dom import minidom
from xml.dom.minidom import parseString

logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(message)s',datefmt = '%a, %d %b %Y %H:%M%S',filename='/var/log/GetHoraris.log',filemode='w' )
logging.info('Start horaris telestany')
try:
    server = SOAPProxy('http://213.151.114.85:8082/')
    horaris =  server.GetHoraris("Telestany")
    hora = parseString(horaris)
    logging.debug(horaris)
    HoraActual = strftime("%H:%M", time.localtime(time.time()))
    Apagar = 0

    if len(hora.getElementsByTagName("hora")) > 0:
	HoraApagar = "23:59"
	for horari in hora.getElementsByTagName("hora"):
	    horaH = horari.attributes["HoraE"].value
	    horaS = horari.attributes["HoraS"].value
	    print horaH
	    print horaS
	    print HoraActual
	    
	    if (timedelta(hours= int(HoraActual.split(':')[0]), minutes=int(HoraActual.split(':')[1])) > timedelta(hours= int(horaH.split(':')[0]), minutes=int(horaH.split(':')[1]))) and (timedelta(hours= int(HoraActual.split(':')[0]), minutes=int(HoraActual.split(':')[1])) < timedelta(hours= int(horaS.split(':')[0]), minutes=int(horaS.split(':')[1]))):
		Apagar = 1
		if timedelta(hours= int(horaS.split(':')[0]), minutes=int(horaS.split(':')[1])) < timedelta(hours= int(HoraApagar.split(':')[0]), minutes=int(HoraApagar.split(':')[1])):
		   HoraApagar = horaS 
	    else:
		logging.info("Hauria d'estar tancat!")
	logging.info("Shauria d'apagar a les :"+HoraApagar)
	value = "shutdown -h "+HoraApagar+" &"
        logging.info(value)
	os.system(value)
    if (Apagar == 0):
	value = "shutdown -h now &"
	logging.info(value)
	os.system(value)
except:
    logging.debug(sys.exc_info()[0])