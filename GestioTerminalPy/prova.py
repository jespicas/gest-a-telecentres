#!/usr/bin/env python

import pygtk
pygtk.require("2.0")
import gtk
import gobject

class Ventana:

    def __init__(self):

        # La ventana
        self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.ventana.set_title("Ventana")
        self.ventana.set_size_request(640, 480)
        self.ventana.connect("delete_event", self.delete_event)

        # La lista
        liststore = gtk.ListStore(str,bool)
        # Los elementos de la lista
        liststore.append(["Uno",True])
        liststore.append(["Dos",False])

        # el contenedor de las filas
        treeview = gtk.TreeView()
        # moldear el contenedor
        treeview.set_model(liststore)

        # Crear la columna para la lista
        treeview.append_column(gtk.TreeViewColumn('Tus archivos', gtk.CellRendererText(), text=0))

        # Barras de desplazamiento para el contenedor
        scroll = gtk.ScrolledWindow()
        scroll.add(treeview)

        self.ventana.add(scroll)
        self.ventana.show_all()

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def main(self):
        gtk.main()

if __name__ == "__main__":
    miventana = Ventana()
    miventana.main()