#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygtk
pygtk.require('2.0')
import gtk
from gtk import glade

import src.frm_okydoky as frm_okydoky
import src.frm_login as frm_login


class MiApp:
    def __init__(self):
        #parse referente al XML remplace ".glade" por el nombre
        #del archivo generado por glade que usara
        self.xml = glade.XML('data/okeyko.glade')

        #Aplicacion principal
        #llame aqui a todas las ventanas que utilizara por ejemplo:
        self.frm_okydoky = frm_okydoky.Form(self.xml)
        self.frm_login = frm_login.Form(self.xml)
        self.frm_okydoky.show(True)
        self.frm_login.show(True)

    def main(self):
        #pasar el control principal a GTK
        gtk.main()


    def destroy(self):
        #detener la ejecucion de la aplicacion
        gtk.main_quit()


if __name__ == "__main__":
    app = MiApp()
    app.main()
