import SOAPpy
import sqlite3
import time
import logging
from datetime import datetime,date, timedelta
from SOAPpy import SOAPProxy
from time import gmtime, strftime

def GetUser(numuser):
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    c.execute (" select * from Usuaris where Targeta = '%s' " % numuser)
    
    IdUSer = ""
    #print numuser
    for row in c:
		IdUSer = row[0]
    return IdUSer

def GetUserName(numuser):
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    c.execute (" select * from Usuaris where Targeta = '%s' " % numuser)
    
    IdUSer = ""
    #print numuser
    for row in c:
		IdUSer = row[1] + " " + row[2] + " " + row[3]
    return IdUSer

def AddLogLloc(IdUser,Hora,Estat,Lloc):
    logging.debug("Entra AddLog Lloc IdUSer:"+str(IdUser)+" Hora "+str(Hora)+" Estat:" + str(Estat))
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    Temps = GetTime(IdUser)
    values = ( strftime("%Y-%m-%d", time.localtime(time.time())) + " 00:00:00", IdUser, Estat )
    c.execute ("select * from Log where Temps >= ? and IdUsuari = ? and ESTAT = ?", values)
    logging.debug("select * from Log where Temps >= "+ strftime("%Y-%m-%d", time.localtime(time.time()))+ " and IdUsuari = "+str(IdUser)+" and ESTAT = "+ str(Estat))
    if ( c.fetchone() == None ):
	logging.debug('c.fechone() igual a None')
	if ( Temps != 0 ):
	    logging.debug('Temps diferent 0')
	    if ( Estat == "VIU"):
		 Temps = Temps - 1
	else:
	    logging.debug('Else Temps diferent 0 posem temps 0')
	    Temps = 0
	c.execute ("insert into Log VALUES (?,?,?,?,?)",[(IdUser),(Hora),(Temps),(Estat),(Lloc)])
	conn.commit()
	logging.debug('Insert into Log ')
	conn.close()
    else:
	logging.debug('c.fetchone diferent a None')
	if (Temps != 0):
	    logging.debug('Temps diferent 0')
	    if ( Estat == "VIU"):
	   	 Temps = Temps - 1
	else:
	    logging.debug('Temps  0')
	    Temps = 0
	c.execute ("select * from Log where Temps >= ? and IdUsuari = ? and ESTAT = ?", values)
	if (Estat == "ENTRA" or Estat == "SURT"):
		c.execute("insert into Log VALUES (?,?,?,?)",[(IdUser),(Hora),(Temps),(Estat)])
		conn.commit()
	else:
		HoraAntiga = c.fetchone()[1]
		logging.debug('Hora antiga' + str(HoraAntiga))	
		values = ( Hora,Temps, IdUser, HoraAntiga, Estat )
		c.execute ("UPDATE Log SET Temps = ?, Quant = ? where IdUsuari = ? and Temps = ? and Estat = ?", values)	
		conn.commit()
		logging.debug('Updated UPDATE Log SET Temps = '+str(Hora)+', Quant = '+str(Temps)+' where IdUsuari = '+str(IdUser)+' and Temps ='+ str(HoraAntiga)+'  and Estat = '+ str(Estat))
	conn.close()
    
    logging.debug('Temps ' + str(Temps))       
    return Temps

	
def AddLog(IdUser,Hora,Estat):
    logging.debug("Entra AddLog IdUSer:"+str(IdUser)+" Hora "+str(Hora)+" Estat:" + str(Estat))
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    Temps = GetTime(IdUser)
    values = ( strftime("%Y-%m-%d", time.localtime(time.time())) + " 00:00:00", IdUser, Estat )
    c.execute ("select * from Log where Temps >= ? and IdUsuari = ? and ESTAT = ?", values)
    logging.debug("select * from Log where Temps >= "+ strftime("%Y-%m-%d", time.localtime(time.time()))+ " and IdUsuari = "+str(IdUser)+" and ESTAT = "+ str(Estat))
    if ( c.fetchone() == None ):
	logging.debug('c.fechone() igual a None')
	if ( Temps != 0 ):
	    logging.debug('Temps diferent 0')
	    if ( Estat == "VIU"):
		 Temps = Temps - 1
	else:
	    logging.debug('Else Temps diferent 0 posem temps 0')
	    Temps = 0
	c.execute ("insert into Log (IdUsuari,Temps,Quant) VALUES (?,?,?,?)",[(IdUser),(Hora),(Temps),(Estat)])
	conn.commit()
	logging.debug('Insert into Log ')
	conn.close()
    else:
	logging.debug('c.fetchone diferent a None')
	if (Temps != 0):
	    logging.debug('Temps diferent 0')
	    if ( Estat == "VIU"):
	   	 Temps = Temps - 1
	else:
	    logging.debug('Temps  0')
	    Temps = 0
	c.execute ("select * from Log where Temps >= ? and IdUsuari = ? and ESTAT = ?", values)
	if (Estat == "ENTRA" or Estat == "SURT"):
		c.execute("insert into Log (IdUsuari,Temps,Quant)  VALUES (?,?,?,?)",[(IdUser),(Hora),(Temps),(Estat)])
		conn.commit()
	else:
		HoraAntiga = c.fetchone()[1]
		logging.debug('Hora antiga' + str(HoraAntiga))	
		values = ( Hora,Temps, IdUser, HoraAntiga, Estat )
		c.execute ("UPDATE Log SET Temps = ?, Quant = ? where IdUsuari = ? and Temps = ? and Estat = ?", values)	
		conn.commit()
		logging.debug('Updated UPDATE Log SET Temps = '+str(Hora)+', Quant = '+str(Temps)+' where IdUsuari = '+str(IdUser)+' and Temps ='+ str(HoraAntiga)+'  and Estat = '+ str(Estat))
	conn.close()
    
    logging.debug('Temps ' + str(Temps))       
    return Temps

def GetTime(IdUser):
    logging.debug('GetTime' + str(IdUser))
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    
    values = ( strftime("%Y-%m-%d", time.localtime(time.time())) + " 00:00:00", IdUser, )
    c.execute ("select * from Log where Temps >= ? and IdUsuari = ? order by Temps DESC", values)
    logging.debug( "select * from Log where Temps >= "+ strftime("%Y-%m-%d", time.localtime(time.time())) + " 00:00:00" +" and IdUsuari = "+ str(IdUser)+" order by Temps DESC")
    if ( c.fetchone() == None):
	logging.debug("c.fetchon == None")
	c2 = conn.cursor()
	c2.execute ('select * from tarja where IdUsuari = ?', [(IdUser)])
	logging.debug("select * from tarja where IdUsuari ="+str(IdUser))
	#print c2.fetchone()
	if ( c2.fetchone() == None):
	    #print "entra"
	    logging.debug("No ha trobat tarja from idUsuari :" + str(IdUser))
	    Quants = 0
	else:
	    c2.execute ('select * from tarja where IdUsuari = ?', [(IdUser)])
	    logging.debug("Ha trobat Informacio taula tarja IdUsuari " + str(IdUser))
	    Quants = c2.fetchone()[2]
	    logging.debug(str(Quants))
    else:
	c.execute ("select * from Log where Temps >= ? and IdUsuari = ? order by Temps DESC", values)
	logging.debug("Ha trobat Temps de lUsuari:" + str(IdUser))
	Quants = c.fetchone()[2]
    conn.close()
    logging.debug(str(Quants))
    return Quants

def CrearUsuaris():
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()    
    c.execute (" select * from Usuaris where Actiu = 1 and targeta != ''")
    #var = """<?xml version="1.0" encoding="UTF-8"?>"""
    var =  "<usuaris>"
    for row in c:
	var = var + "<usuari id = '" + str(row[0] + 1000) + "'"
	var = var + " nom= '" +row[16]+"' />"
	
    var = var + "</usuaris>"    
    return var

def GetUsuarisEsborrar():
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    c.execute (" select * from Usuaris where Actiu = 0 and targeta != ''")
    var =  "<usuaris>"
    for row in c:
	var = var + "<usuari id = '" + str(row[0] + 1000) + "'"
	var = var + " nom= '" +row[16]+"' />"
    var = var + "</usuaris>"    
    return var
	
def GetHoraris(Lloc):
    dicDays = {'MONDAY':'Dilluns','TUESDAY':'Dimarts','WEDNESDAY':'Dimecres','THURSDAY':'Dijous', \
'FRIDAY':'Divendres','SATURNDAY':'Dissabte','SUNDAY':'Diumenge'}
    DiaSetmana =  dicDays[strftime("%A", time.localtime(time.time())).upper()]
    conn = sqlite3.connect('/usr/share/local/telestany/telestany.sqlite')
    c = conn.cursor()
    c.execute (" select * from HorarisVariables where Dia = '"+ strftime("%d/%m/%Y", time.localtime(time.time())) + "' and Lloc='"+Lloc+"'")
    var =  "<hores>"
    for row in c:
	var = var + "<hora HoraE = '" + str(row[1])+"' HoraS = '" + str(row[2])+"' />"
    c.execute ("select * from HorarisFix where Lloc = '"+Lloc+"' and dia like '%"+DiaSetmana+"%'")
    for row in c:
	var = var + "<hora HoraE = '" + str(row[0])+"' HoraS = '" + str(row[1])+"' />"
    var = var + "</hores>"    
    return var
	

    
if __name__ == "__main__":    
    server = SOAPpy.SOAPServer(("213.151.114.85", 8082))
    logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(message)s',datefmt = '%a, %d %b %Y %H:%M%S',filename='/var/log/TelecentreWebService.log',filemode='w' )
    logging.info('Start webService')
    #logging.debug('Prova a veure que passa')
    logging.info('Finished')
    server.registerFunction(GetUser)
    logging.info('GetUser registrar')
    server.registerFunction(GetUserName)
    logging.info('GetUserName registar')
    server.registerFunction(AddLogLloc)
    logging.info('AddLogLloc registrar')
    server.registerFunction(AddLog)
    logging.info('AddLog registrar')
    server.registerFunction(GetTime)
    logging.info('GetTime registrar')
    server.registerFunction(CrearUsuaris)
    logging.info('CrearUsuaris registrar')
    server.registerFunction(GetUsuarisEsborrar)
    logging.info('GetUsuarisEsborrar registrar')
    server.registerFunction(GetHoraris)
    logging.info('GetHoraris registrar')    
    server.serve_forever()

