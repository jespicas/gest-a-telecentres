# SimpleGladeApp.py
# Module that provides an object oriented abstraction to pygtk and libglade.
# Copyright (C) 2004 Sandino Flores Moreno

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA

import os
import platform
import sys
import gtk
import gtk.glade
import pygtk
pygtk.require("2.0")
import threading
from threading import Thread
import sys
import os
import struct
import socket


class GestioTerminalsApp(object):       
	
        def __init__(self):
	    self.builder = gtk.Builder()
	    self.builder.add_from_file("GestioTerminalsFrm.glade")
	    self.window = self.builder.get_object("window1")
            self.treeview = self.builder.get_object("treeview1")            
            self.liststore = gtk.ListStore(bool,str,gtk.gdk.Pixbuf,str,str)
            filename = "button_20x20.png"
            red = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)
            filename = "greenbutton_20x20.png"
            green = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)
            filename = "orange_20x20.png"
            orange = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)            
#            self.liststore.append ([True,"posarem text",red,"prova",""])
#            self.liststore.append ([False,"posarem 1text",green,"prova2",""])
            self.cell = gtk.CellRendererToggle()
            self.treeview.set_model(self.liststore)
            hilo = threading.Thread(target=self.Server_Espera_Pc,args=(self.treeview))
            hilo.start()                
            
       # Crear la columna para la lista

            self.treeview.append_column(gtk.TreeViewColumn('chk', gtk.CellRendererToggle(), active=0))
            self.treeview.append_column(gtk.TreeViewColumn('Tus archivos', gtk.CellRendererText(), text=1))
            self.treeview.append_column(gtk.TreeViewColumn('Status', gtk.CellRendererPixbuf(), pixbuf=2))
            column = gtk.TreeViewColumn('IP', gtk.CellRendererText(), text=3)
            column.set_visible(False)
            self.treeview.append_column(column)
            self.treeview.append_column(gtk.TreeViewColumn('Users', gtk.CellRendererText(), text=4))

        # Barras de desplazamiento para el contenedor
            scroll = gtk.ScrolledWindow()
            scroll.add(self.treeview)
            self.entry1 = self.builder.get_object("entry1")
            self.button1 = self.builder.get_object("button1")
            self.button2 = self.builder.get_object("button2")
            self.radiobutton1 = self.builder.get_object("radiobutton1")
            self.radiobutton2 = self.builder.get_object("radiobutton2")
            self.treeview.connect("row-activated",self.on_treeview_row_activated)
            self.button1.connect("clicked",self.on_button1_clicked)
            self.button2.connect("clicked",self.on_button2_clicked)
            self.window.connect("destroy",self.on_window_destroy)
	    self.window.show_all()
            
        def on_treeview_row_activated(self,widget,path,column):
                print "eis he triat alguna cosa ? "
                (model,iter)=self.treeview.get_selection().get_selected()
                print model
                print iter
                if iter != None:
                        print list(model[iter])
                if (model[iter][0] == True):
                        model.set(iter,0,False)
                       # filename = "greenbutton_20x20.png"
                       # green = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)                              
                       # model.set(iter,2,green)
                else:
                       # filename = "button_20x20.png"
                       # red = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)                              
                        model.set(iter,0,True)
                       # model.set(iter,2,red)
                        
        def on_button1_clicked(self,widget):
                print "eeeei!"
                lists = self.treeview.get_model()
                print lists
                print self.treeview.get_selection().get_tree_view()
                column = self.treeview.get_selection().get_tree_view().get_column(1)
                print lists[0].iter
                print len(lists)
                for iter in lists:
                        if iter[0] == True:
                                s = socket.socket()
                                print iter[3]
                                s.connect((iter[3],9999))
                                d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                                #IP =  socket.inet_ntoa("172.17.14.18")
                                #host = socket.gethostname()
                                print self.entry1.get_text()
                                s.send("MESSAGE")
                                
                                rebuc = s.recv(1024)
                                if rebuc == "REBUT":
                                        s.send(self.entry1.get_text())
                               # print rebuc
                               # print "adios"
                                s.close()                                
                        print iter[0]

        def on_button2_clicked(self,widget):
                print "eeeei!"
                lists = self.treeview.get_model()
                print lists
                print self.treeview.get_selection().get_tree_view()
                column = self.treeview.get_selection().get_tree_view().get_column(1)
                print lists[0].iter
                print len(lists)
                for iter in lists:
                        if iter[0] == True:
                                if  self.radiobutton1.get_active():
                                        os.system("plink -i id_rsa.ppk root@"+iter[3]+" shutdown -h now")                
                                elif self.radiobutton2.get_active():
                                        os.system("plink -i id_rsa.ppk root@"+iter[3]+" shutdown -r now")        
                                
                #lists.append([False,"Prova 2"])                
        def on_window_destroy(self,widget):
                sys.exit(0)
        
        def Server_Espera_Pc(text):
                gtk.gdk.threads_enter()
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', "eth0"[:15]))[20:24])	
		server.bind(("172.17.14.48", 9999))
		server.listen(1)
		print "Esperando clientes..."
                print text
		# bucle para atender clientes
		while 1:
			# Se espera a un cliente
			socket_cliente, datos_cliente = server.accept()
                        #hilo = threading.Thread(target=text.ClientServer,args=(text,socket_cliente))
                        #hilo.start() 
			# Se crea la clase con el hilo y se arranca.
                        peticion = socket_cliente.recv(1024)
                        print peticion
                        ValorColumna = ""
                        status = gtk.gdk.Pixbuf                        
                        if (peticion.split('|')[0] == "OBRO"):
                                ValorColumna = peticion.split('|')[1]
                                print ValorColumna
                                filename = "orange_20x20.png"
                                status = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)
                                lists = text.treeview.get_model()
                                lists.append([False,ValorColumna,status,datos_cliente[0],""])
                                i = 0
                                Trobat = False
                                for iter in lists:
                                        print iter[3]
                                        if (str(iter[3]) == str(datos_cliente[0]) ):
                                                lists.set(lists[i].iter,2,status)
                                                Trobat = True
                                        i = i + 1
                                if Trobat == False:
                                        lists.append([False,ValorColumna,status,datos_cliente[0],""])        
                        if (peticion.split('|')[0] == "USER"):
                                ValorColumna = peticion.split('|')[1]
                                filename = "greenbutton_20x20.png"
                                status = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)                        
                                lists = text.treeview.get_model()
                                print lists
                                print text.treeview.get_selection().get_tree_view()
                                column = text.treeview.get_selection().get_tree_view().get_column(1)
                                #print lists[0].iter
                                print len(lists)
                                i = 0
                                Trobat = False
                                for iter in lists:
                                        if (str(iter[3]) == str(datos_cliente[0]) ):
                                                lists.set(lists[i].iter,2,status)
                                                lists.set(lists[i].iter,4,peticion.split('|')[2])
                                                Trobat = True
                                        i = i + 1
                                if Trobat == False:
                                        lists.append([False,ValorColumna,status,datos_cliente[0],peticion.split('|')[2]])        
                        if (peticion.split('|')[0] == "SURTO"):
                                filename = "orange_20x20.png"
                                status = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)                        
                                lists = text.treeview.get_model()
                                print lists
                                print text.treeview.get_selection().get_tree_view()
                                column = text.treeview.get_selection().get_tree_view().get_column(1)
                                print lists[0].iter
                                print len(lists)
                                i = 0
                                for iter in lists:
                                        if (str(iter[3]) == str(datos_cliente[0]) ):
                                                lists.set(lists[i].iter,2,status)
                                                lists.set(lists[i].iter,4,peticion.split('|')[2])
                                        i = i + 1
                        if (peticion.split('|')[0] == "APAGO"):
                                filename = "button_20x20.png"
                                status = gtk.gdk.pixbuf_new_from_file(unicode(os.getcwd(),sys.getfilesystemencoding())+'\\'+filename)                        
                                lists = text.treeview.get_model()
                                print lists
                                print text.treeview.get_selection().get_tree_view()
                                column = text.treeview.get_selection().get_tree_view().get_column(1)
                                print lists[0].iter
                                print len(lists)
                                i = 0
                                for iter in lists:
                                        if (str(iter[3]) == str(datos_cliente[0]) ):
                                                lists.set(lists[i].iter,2,status)                                                
                                        i = i + 1                                         
                        #rebut =  socket_cliente.recv(1024)
                        #print rebut
                        socket_cliente.send("REBUT")
                        print datos_cliente[0]
                        socket_cliente.close()
			#hilo = Cliente(socket_cliente, datos_cliente,text)                        
			#hilo.start()
                gtk.gdk.threads_leave()
                
        def ClientServer(text,socketcl,datoscli):
                gtk.gdk.threads_enter()
                seguir = True
                while seguir:
                        # Espera por datos
                        print type(text)
                        #peticion = socketcl.recv(1024)
                        #print peticion
                        #print type(self.treeview)
                        #print type(self.treeview.treeview)
                        #print self.treeview.treeview.get_model()
                        #lists = self.treeview.treeview.get_model()
                        #lists.append([False,"blabla"])
                        #self.socket.send("REBUT")
                        # Contestacion a "hola"
                        #if ("MESSAGE"==peticion):
                        #    print str(self.datos)+ " envia VIU: contesto"
                        #    self.socket.send("REBUT")
                        #    rec = self.socket.recv(1024)
                        #    os.system('gxmessage "'+str(rec)+'" &')
                        #    print rec
                        #    self.socket.close()
                        #    print "desconectado "+str(self.datos)
                        seguir = False                
                gtk.gdk.threads_leave()       
class Server(Thread):
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', "eth0"[:15]))[20:24])
                if platform.system() == 'Windows':
                        i =0
                        for addr in getIPAddresses():
                                if i > 0:
                                        break
                                else:
                                        IP = addr
                                i = i + 1
                else:
        		d = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        		IP =  socket.inet_ntoa(fcntl.ioctl(d.fileno(),0x8915,struct.pack('256s', "eth0"[:15]))[20:24])
                        
		server.bind((IP, 9999))
		server.listen(1)
		print "Esperando clientes..."
   
		# bucle para atender clientes
		while 1:
			# Se espera a un cliente
			socket_cliente, datos_cliente = server.accept()
			# Se escribe su informacion
			print "conectado "+str(datos_cliente)
			# Se crea la clase con el hilo y se arranca.
			hilo = Cliente(socket_cliente, datos_cliente,treeview)
			hilo.start()
	
        def getIPAddresses():
            from ctypes import Structure, windll, sizeof
            from ctypes import POINTER, byref
            from ctypes import c_ulong, c_uint, c_ubyte, c_char
            MAX_ADAPTER_DESCRIPTION_LENGTH = 128
            MAX_ADAPTER_NAME_LENGTH = 256
            MAX_ADAPTER_ADDRESS_LENGTH = 8
            class IP_ADDR_STRING(Structure):
                pass
            LP_IP_ADDR_STRING = POINTER(IP_ADDR_STRING)
            IP_ADDR_STRING._fields_ = [
                ("next", LP_IP_ADDR_STRING),
                ("ipAddress", c_char * 16),
                ("ipMask", c_char * 16),
                ("context", c_ulong)]
            class IP_ADAPTER_INFO (Structure):
                pass
            LP_IP_ADAPTER_INFO = POINTER(IP_ADAPTER_INFO)
            IP_ADAPTER_INFO._fields_ = [
                ("next", LP_IP_ADAPTER_INFO),
                ("comboIndex", c_ulong),
                ("adapterName", c_char * (MAX_ADAPTER_NAME_LENGTH + 4)),
                ("description", c_char * (MAX_ADAPTER_DESCRIPTION_LENGTH + 4)),
                ("addressLength", c_uint),
                ("address", c_ubyte * MAX_ADAPTER_ADDRESS_LENGTH),
                ("index", c_ulong),
                ("type", c_uint),
                ("dhcpEnabled", c_uint),
                ("currentIpAddress", LP_IP_ADDR_STRING),
                ("ipAddressList", IP_ADDR_STRING),
                ("gatewayList", IP_ADDR_STRING),
                ("dhcpServer", IP_ADDR_STRING),
                ("haveWins", c_uint),
                ("primaryWinsServer", IP_ADDR_STRING),
                ("secondaryWinsServer", IP_ADDR_STRING),
                ("leaseObtained", c_ulong),
                ("leaseExpires", c_ulong)]
            GetAdaptersInfo = windll.iphlpapi.GetAdaptersInfo
            GetAdaptersInfo.restype = c_ulong
            GetAdaptersInfo.argtypes = [LP_IP_ADAPTER_INFO, POINTER(c_ulong)]
            adapterList = (IP_ADAPTER_INFO * 10)()
            buflen = c_ulong(sizeof(adapterList))
            rc = GetAdaptersInfo(byref(adapterList[0]), byref(buflen))
            if rc == 0:
                for a in adapterList:
                    adNode = a.ipAddressList
                    while True:
                        ipAddr = adNode.ipAddress
                        if ipAddr:
                            yield ipAddr
                        adNode = adNode.next
                        if not adNode:
                            break
        	
class Cliente(Thread):
    def __init__(self, socket_cliente, datos_cliente,treeview):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos = datos_cliente
        self.treeview = treeview
 
    # Bucle para atender al cliente.       
    def run(self):
      # Bucle indefinido hasta que el cliente envie "VIU"
      seguir = True
      while seguir:
         # Espera por datos
         peticion = self.socket.recv(1024)
         print peticion
         print type(self.treeview)
         print type(self.treeview.treeview)
         print self.treeview.treeview.get_model()
         lists = self.treeview.treeview.get_model()
         lists.append([False,"blabla"])
         self.socket.send("REBUT")
         # Contestacion a "hola"
         #if ("MESSAGE"==peticion):
         #    print str(self.datos)+ " envia VIU: contesto"
         #    self.socket.send("REBUT")
	 #    rec = self.socket.recv(1024)
	 #    os.system('gxmessage "'+str(rec)+'" &')
	 #    print rec
	 #    self.socket.close()
         #    print "desconectado "+str(self.datos)
         seguir = False
             
if __name__ == "__main__":
        gtk.gdk.threads_init()
	app = GestioTerminalsApp()
	gtk.main()
        
