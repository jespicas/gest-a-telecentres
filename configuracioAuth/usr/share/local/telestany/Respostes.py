#!/usr/bin/env python

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#  ExampleScreenlet (c) RYX 2007 <ryx@ryxperience.com>
#
# INFO:
# - a simple example for creating a Screenlet
# 
# TODO:
# - make a nice Screenlet from this example ;) ....

import logging
import SOAPpy
from SOAPpy import SOAPProxy
import socket
import sys
import os
import fcntl
import struct
import xml.sax
import xml.sax.handler
import array
import platform
import commands

from threading import Thread
from xml.dom import minidom
from xml.dom.minidom import parseString

# global constants.  If you don't like 'em here,
# move 'em inside the function definition.
SIOCGIFCONF = 0x8912
MAXBYTES = 8096

def localifs():
    """
    Used to get a list of the up interfaces and associated IP addresses
    on this machine (linux only).

    Returns:
        List of interface tuples.  Each tuple consists of
        (interface name, interface IP)
    """
    global SIOCGIFCONF
    global MAXBYTES

    arch = platform.architecture()[0]

    # I really don't know what to call these right now
    var1 = -1
    var2 = -1
    if arch == '32bit':
        var1 = 32
        var2 = 32
    elif arch == '64bit':
        var1 = 16
        var2 = 40
    else:
        raise OSError("Unknown architecture: %s" % arch)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', '\0' * MAXBYTES)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        sock.fileno(),
        SIOCGIFCONF,
        struct.pack('iL', MAXBYTES, names.buffer_info()[0])
        ))[0]

    namestr = names.tostring()
    return [(namestr[i:i+var1].split('\0', 1)[0], socket.inet_ntoa(namestr[i+20:i+24])) \
            for i in xrange(0, outbytes, var2)]

class Server(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		ifaces = localifs()
		for iface in ifaces:
			if ( iface[0] != 'lo'):
				eth = iface[0]
		try:
			IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', eth[:15]))[20:24])
		except:
			logging.debug("Error eth")
		server.bind((IP, 9998))
		server.listen(1)
		logging.debug('Esperent Clients')
		print "Esperando clientes..."
   
		# bucle para atender clientes
		while 1:
		 
			# Se espera a un cliente
			socket_cliente, datos_cliente = server.accept()
			
			# Se escribe su informacion
			print "conectado "+str(datos_cliente)
			
			# Se crea la clase con el hilo y se arranca.
			hilo = Cliente(socket_cliente, datos_cliente)
			hilo.start()
		
class Cliente(Thread):
    def __init__(self, socket_cliente, datos_cliente):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos = datos_cliente
 
    # Bucle para atender al cliente.       
    def run(self):
      # Bucle indefinido hasta que el cliente envie "VIU"
      seguir = True
      while seguir:
         # Espera por datos
         peticion = self.socket.recv(1024)
         print peticion
         # Contestacion a "hola"
	 if ("ONLINE"==peticion):
    	     host = socket.gethostname()	     
             self.socket.send("REBUT|"+host)
	     self.socket.close()
             print "desconectado "
             seguir = False
	 if ("REBOOT"==peticion):
    	     host = socket.gethostname()	     
             self.socket.send("REBUT|"+host)
	     self.socket.close()
             print "desconectado "
	     os.system('reboot')
             seguir = False	     
	 if ("SHUTDOWN"==peticion):
    	     host = socket.gethostname()	     
             self.socket.send("REBUT|"+host)
	     self.socket.close()
             print "desconectado "
	     os.system('shutdown -h now')
             seguir = False
	 if ("ENDSESSIO"==peticion):
    	     host = socket.gethostname()	     
             self.socket.send("REBUT|"+host)
	     self.socket.close()
	     Pid = commands.getoutput('pidof gnome-session')
	     Error = 'kill '+str(Pid)
	     os.system(Error)
             print "desconectado "
             seguir = False
	 if ("UPDATEUSERS"==peticion):
    	     host = socket.gethostname()	     
             self.socket.send("REBUT|"+host)
	     self.socket.close()
	     os.system('/usr/bin/python /usr/share/local/telestany/users.py &')
             print "desconectado "
             seguir = False
	     
# If the program is run directly or passed as an argument to the python
# interpreter then create a Screenlet instance and show it
if __name__ == "__main__":
	# create new session
	logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(message)s',datefmt = '%a, %d %b %Y %H:%M%S',filename='/var/log/Respostes.log',filemode='w' )
	logging.info('Start Respostes')
	logging.debug('Prova a veure que passa')
	hilo = Server()
	hilo.start()
	logging.debug('Fil server executat')
	logging.info('Finished')
