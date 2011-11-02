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

import screenlets
import logging
from screenlets.options import *
from screenlets.options import create_option_from_node
from screenlets import DefaultMenuItem
import pango
import gobject
import gtk
import SOAPpy
from SOAPpy import SOAPProxy
import time
import datetime
import socket
import time
import sys
import os
import fcntl
import struct
import xml.sax
import xml.sax.handler
import array
import platform

from time import gmtime,strftime
from datetime import datetime,date, timedelta
from threading import Thread
from xml.dom import minidom
from xml.dom.minidom import parseString

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
    
class ControlTempsScreenlet (screenlets.Screenlet):
	"""A simple example of how to create a Screenlet"""
	
	# default meta-info for Screenlets (should be removed and put into metainfo)
	__name__	= 'ExampleScreenlet'
	__version__	= '0.4.1'
	__author__	= 'RYX and Whise'
	__desc__	= __doc__	# set description to docstring of class
	
	# editable options (options that are editable through the UI)
	test_text = 'Hi.. im a screenlet'
	demo_text = ''
	demo_number = ''
	int_example = 1
	bool_example = True
	time_example =  (7, 30, 0)
	account_example =  ('','')
	color_example =(0.0, 0.0, 0.0, 1)
	font_example = "FreeSans Bold 15"
	image_example = ''
	file_example = ''
	directory_example = ''
	list_example = ('','')
	hover = False
	number = 0
	IdUser = ""
	horaDescomptar = 0
	Apagar = 0
	horaris = ''
	hora = ''
	config = minidom.parse(unicode("/usr/share/local/telestany/",sys.getfilesystemencoding())+'/config.xml')
	
	# constructor
	def __init__ (self, **keyword_args):
		#call super (width/height MUST match the size of graphics in the theme)
		screenlets.Screenlet.__init__(self, width=238, height=191, 
			uses_theme=True, **keyword_args)
		# set theme
		self.theme_name = "png"
		config = minidom.parse(unicode("/usr/share/local/telestany/",sys.getfilesystemencoding())+'/config.xml')
		server = SOAPProxy('http://'+config.getElementsByTagName('WebServer')[0].attributes["IP"].value+':'+config.getElementsByTagName('WebServer')[0].attributes["Port"].value+'/')
		horaris =  server.GetHoraris(config.getElementsByTagName('Lloc')[0].attributes["Nom"].value)
		logging.debug("Horaris"+horaris)
		hora = parseString(horaris)
		HoraActual = strftime("%H:%M", time.localtime(time.time()))
		if len(hora.getElementsByTagName("hora")) > 0:
			HoraApagar = strftime("%H:%M", time.localtime(time.time()))
			for horari in hora.getElementsByTagName("hora"):
			    horaH = horari.attributes["HoraE"].value
			    horaS = horari.attributes["HoraS"].value
			    print horaH
			    print horaS
			    print HoraActual
			    
			    if (timedelta(hours= int(HoraActual.split(':')[0]), minutes=int(HoraActual.split(':')[1])) > timedelta(hours= int(horaH.split(':')[0]), minutes=int(horaH.split(':')[1]))) and (timedelta(hours= int(HoraActual.split(':')[0]), minutes=int(HoraActual.split(':')[1])) < timedelta(hours= int(horaS.split(':')[0]), minutes=int(horaS.split(':')[1]))):
				#Apagar = 1
				if timedelta(hours= int(horaS.split(':')[0]), minutes=int(horaS.split(':')[1])) < timedelta(hours= int(HoraApagar.split(':')[0]), minutes=int(HoraApagar.split(':')[1])):
				   HoraApagar = horaS 
			    else:
				logging.info("Hauria d'estar tancat!")
		else:
                        HoraApagar = strftime("%H:%M", time.localtime(time.time()))
		self.IdUser = server.GetUser(str(os.environ['USER']))
		#self.IdUser = server.GetUser(8636071700716196)
		logging.debug("HoraApagar:"+HoraApagar)
		logging.debug("HoraActual:"+HoraActual)
		#HoraApagar = "15:00"
		TempsTarja = timedelta(minutes= server.AddLogLloc(self.IdUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'ENTRA',config.getElementsByTagName('Lloc')[0].attributes["Nom"].value))
		logging.debug("Temps Tarja:"+str(TempsTarja))
		tmHoraApagar = timedelta(hours=int(HoraApagar.split(':')[0]),minutes=int(HoraApagar.split(':')[1]))
		tmHoraActual = timedelta(hours=int(HoraActual.split(':')[0]),minutes=int(HoraActual.split(':')[1]))
		horaDescomptar = TempsTarja - (tmHoraApagar - tmHoraActual)
		logging.debug("HoraDEscomptar"+str(horaDescomptar))
		try:
			s = socket.socket()
			s.settimeout(5)
			serverm = config.getElementsByTagName('GestorServer')[0].attributes["IP"].value
			logging.debug("Abans Connexio Server "+serverm)
			s.connect((serverm,9999))
			#d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			#IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', config.getElementsByTagName('Ethernet')[0].attributes["Nom"].value[:15]))[20:24])
			host = socket.gethostname()
			User = server.GetUserName(self.IdUser)
			if ( User == ""):
				User = str(os.environ['USER'])
			s.send("USER|"+host+"|"+User)
			logging.debug("Send at "+serverm+":USER|"+host+"|"+User)
			rebuc = s.recv(1024)
			print rebuc
			logging.debug("Rebut: "+rebuc)
			print "adios"
			s.close()
		except:
			logging.debug(' No trobat servidor')
			pass

		#self.IdUser = server.GetUser(8636071700716196)
		logging.debug(' Login:'+ str(os.environ['USER'])+' return GetUSer:' + str(self.IdUser))
		self.number = str(horaDescomptar)
		hora = self.number.split(':')[0]
		minut = self.number.split(':')[1]
		if hora+':'+minut == '0:00':
			os.system('gxmessage "S\'ha acabat el temps" &')
			server.AddLogLloc(self.IdUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'SURT',config.getElementsByTagName('Lloc')[0].attributes["Nom"].value)
			os.system("gnome-session-save --kill --force-logout")
		# add option group

		# ADD a 1 second (1000) TIMER
		self.timer = gobject.timeout_add( 1000, self.update)

		#Also add options from xml file for example porpuse
		#self.init_options_from_metadata() 
	
	def update (self):
		segons = int(self.number.split(':')[2])
		minuts = int(self.number.split(':')[1])
		hora = int(self.number.split(':')[0])

		#logging.debug( str(segons))
		if segons == 0:
			segons = 59
			minuts = minuts - 1
                        config = minidom.parse(unicode("/usr/share/local/telestany/",sys.getfilesystemencoding())+'/config.xml')
                        server = SOAPProxy('http://'+config.getElementsByTagName('WebServer')[0].attributes["IP"].value+':'+config.getElementsByTagName('WebServer')[0].attributes["Port"].value+'/')
                        #self.IdUser = server.Getuser(os.environ['USER'])
                        server.AddLogLloc(self.IdUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'VIU',config.getElementsByTagName('Lloc')[0].attributes["Nom"].value)
			logging.debug("Enviat Temps: Status:VIU")
			if str(hora)+':'+str(minuts) == '0:5':
				os.system('gxmessage "Falten 5 minuts" &')
			if  minuts == 0:
                                hora = hora - 1
                                minuts = 59
                                if str(hora)+':'+str(minuts) == '0:00':
                                        os.system('gxmessage "S\'ha acabat el temps" &')
                                        server.AddLogLloc(self.IdUser,strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),'SURT',config.getElementsByTagName('WebServer')[0].attributes["Lloc"].value)
                #			os.system("gnome-session-save --kill --force-logout")
		else:
			segons = segons - 1
		#logging.debug( str(segons)) 
		self.number = str(hora)+":"+str(minuts)+":"+str(segons)		
		self.redraw_canvas()
		return True # keep running this event	
	
	# ONLY FOR TESTING!!!!!!!!!
	def init_options_from_metadata (self):
		"""Try to load metadata-file with options. The file has to be named
		like the Screenlet, with the extension ".xml" and needs to be placed
		in the Screenlet's personal directory. 
		NOTE: This function always uses the metadata-file relative to the 
			  Screenlet's location, not the ones in SCREENLETS_PATH!!!"""
		#print __file__
		p = __file__.rfind('/')
		mypath = __file__[:p]
		# print mypath
		self.add_options_from_file( mypath + '/' + \
			self.__class__.__name__ + '.xml')	


	def on_after_set_atribute(self,name, value):
		"""Called after setting screenlet atributes"""
		#print name + ' is going to change from ' + str(value)
		pass

	def on_before_set_atribute(self,name, value):
		"""Called before setting screenlet atributes"""
		#print name + ' has changed to ' + str(value)
		pass


	def on_create_drag_icon (self):
		"""Called when the screenlet's drag-icon is created. You can supply
		your own icon and mask by returning them as a 2-tuple."""
		return (None, None)

	def on_composite_changed(self):
		"""Called when composite state has changed"""
		pass

	def on_drag_begin (self, drag_context):
		"""Called when the Screenlet gets dragged."""
		pass
	
	def on_drag_enter (self, drag_context, x, y, timestamp):
		"""Called when something gets dragged into the Screenlets area."""
		pass
	
	def on_drag_leave (self, drag_context, timestamp):
		"""Called when something gets dragged out of the Screenlets area."""
		pass

	def on_drop (self, x, y, sel_data, timestamp):
		"""Called when a selection is dropped on this Screenlet."""
		return False
		
	def on_focus (self, event):
		"""Called when the Screenlet's window receives focus."""
		pass
	
	def on_hide (self):
		"""Called when the Screenlet gets hidden."""
		pass
	
	def on_init (self):
		"""Called when the Screenlet's options have been applied and the 
		screenlet finished its initialization. If you want to have your
		Screenlet do things on startup you should use this handler."""
		#print 'i just got started'
		# add  menu items from xml file
		#self.add_default_menuitems(DefaultMenuItem.XML)
		# add menu item
		#self.add_menuitem("at_runtime", "A")
		# add default menu items
		#self.add_default_menuitems()


#	def on_key_down(self, keycode, keyvalue, event):
#		"""Called when a keypress-event occured in Screenlet's window."""
#		key = gtk.gdk.keyval_name(event.keyval)
#		
#		if key == "Return" or key == "Tab":
#			screenlets.show_message(self, 'This is the ' + self.__name__ +'\n' + 'It is installed in ' + self.__path__)
#	
	def on_load_theme (self):
		"""Called when the theme is reloaded (after loading, before redraw)."""
		pass
	
	def on_menuitem_select (self, id):
		"""Called when a menuitem is selected."""
		if id == "at_runtime":
			screenlets.show_message(self, 'This is an example on a menu created at runtime')
		if id == "at_xml":
			screenlets.show_message(self, 'This is an example on a menu created in the menu.xml')
		pass
	
	def on_mouse_down (self, event):
		"""Called when a buttonpress-event occured in Screenlet's window. 
		Returning True causes the event to be not further propagated."""

		return False
	
	def on_mouse_enter (self, event):
		"""Called when the mouse enters the Screenlet's window."""
		#self.show_tooltip("this is a tooltip , it is set to shows on mouse hover",self.x+self.mousex,self.y+self.mousey)
		#self.hover = True
		#print 'mouse is over me'
		pass
		
	def on_mouse_leave (self, event):
		"""Called when the mouse leaves the Screenlet's window."""
		#self.hide_tooltip()
		#self.hover = False
		#print 'mouse leave'
		pass

	def on_mouse_move(self, event):
		"""Called when the mouse moves in the Screenlet's window."""
		self.redraw_canvas()
		pass

	def on_mouse_up (self, event):
		"""Called when a buttonrelease-event occured in Screenlet's window. 
		Returning True causes the event to be not further propagated."""
		return False
	
	def on_quit (self):
		"""Callback for handling destroy-event. Perform your cleanup here!"""
		self.redraw_canvas()
		pass #return False
		
	def on_realize (self):
		""""Callback for handling the realize-event."""
	
	def on_scale (self):
		"""Called when Screenlet.scale is changed."""
		pass
	
	def on_scroll_up (self):
		"""Called when mousewheel is scrolled up (button4)."""
		pass

	def on_scroll_down (self):
		"""Called when mousewheel is scrolled down (button5)."""
		pass
	
	def on_show (self):
		"""Called when the Screenlet gets shown after being hidden."""
		pass
	
	def on_switch_widget_state (self, state):
		"""Called when the Screenlet enters/leaves "Widget"-state."""
		pass
	
	def on_unfocus (self, event):
		"""Called when the Screenlet's window loses focus."""
		pass
	
	def on_draw (self, ctx):
		# if theme is loaded
		if self.theme:
			# set scale rel. to scale-attribute
			ctx.scale(self.scale, self.scale)
			ctx.set_source_rgba(self.color_example[2], self.color_example[1], self.color_example[0],0.4)	
			if self.hover:
				self.draw_rounded_rectangle(ctx,0,0,20,self.width,self.height)
			self.draw_circle(ctx,0,0,self.width,self.height)
			# TEST: render example-bg into context (either PNG or SVG)
			self.theme.render(ctx, 'example-bg')
			ctx.set_source_rgba( self.color_example[0], self.color_example[1], self.color_example[2],self.color_example[3])
			#self.draw_text(ctx, self.test_text, 20, 20, self.font_example , 20,self.width,pango.ALIGN_LEFT)
			self.draw_text(ctx, str(self.number), 20, 40, self.font_example , 20, self.width,pango.ALIGN_LEFT)
			#self.draw_text(ctx, self.theme_name, 20, 80, self.font_example , 15, self.width,pango.ALIGN_LEFT)

			#self.draw_text(ctx, 'mouse x ' + str(self.mousex ) + ' \n mouse y ' + str(self.mousey ) , 20, 100, self.font_example , 10,self.width,pango.ALIGN_LEFT)
			#print self.get_text_width(ctx, 'mouse x ' + str(self.mousex ) + ' \n mouse y ' + str(self.mousey ) , self.font_example)

			# render svg-file
			#self.theme['example-bg.svg'].render_cairo(ctx)
			# render png-file
			#ctx.set_source_surface(self.theme['example-test.png'], 0, 0)
			#ctx.paint()
	
	def on_draw_shape (self, ctx):
		self.on_draw(ctx)
	
	

class Server(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
                config = minidom.parse(unicode("/usr/share/local/telestany/",sys.getfilesystemencoding())+'/config.xml')
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
		server.bind((IP, 9999))
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
         if ("MESSAGE"==peticion):
             print str(self.datos)+ " envia VIU: contesto"
             self.socket.send("REBUT")
	     rec = self.socket.recv(1024)
	     os.system('gxmessage "'+str(rec)+'" &')
	     print rec
	     self.socket.close()
             print "desconectado "+str(self.datos)
             seguir = False
         if ("SURTSESSIO"==peticion):
             print str(self.datos)+ " "
             self.socket.send("REBUT")
	     rec = self.socket.recv(1024)
	     print rec
	     self.socket.close()
             print "desconectado "+str(self.datos)
	     os.system("gnome-session-save --kill --force-logout")
             seguir = False
	 if ("ONLINE"==peticion):
             self.socket.send("REBUT")
	     self.socket.close()
	     seguir = False

# If the program is run directly or passed as an argument to the python
# interpreter then create a Screenlet instance and show it
if __name__ == "__main__":
	# create new session
	import screenlets.session
	logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s %(levelname)s %(message)s',datefmt = '%a, %d %b %Y %H:%M%S',filename='ControlTemps.log',filemode='w' )
	logging.info('Start Screenlet')
	logging.debug('Prova a veure que passa')
	hilo = Server()
	hilo.start()
	logging.debug('Fil server executat')
	screenlets.session.create_session(ControlTempsScreenlet)
	logging.info('Finished')
