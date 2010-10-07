#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Oky:
    def __init__(self, argv*):
        self.remitent = argv[0]
        self.hora = argv[1],argv[2]
        self.texto = argv[3]
        self.oki_id = argv[4]
        self.avatar = argv[5]
        self.estado = argv[6] #leido
        sel.fav = argv[7] #no se q corno es esto :P
        self.enviado = argv[8]


    def format(self):
        """
            Formateo del texto del mensaje para mostrarlo
            como texto plano
        """
        #no implementado
        pass



class MsjList:
    """
        Clase base contenedora para cualquier grupo de sprites
    """
    def __init__(self):
        self.__mensajes = {}


    def add(self, msj=None):
        if  != None:
            self.__mensajes[msj.oki_id] = mensaje


    def clear(self):
        self.__mensajes.clear()


    def export_to_txt(self, file_name="mensajes.txt"):
        file = open(file_name, 'w')


    # Metodos Especiales
    def __len__(self):
        return len(self.__mensajes)


    def __getitem__(self, key):
        return self.__mensajes[key]


    def __setitem__(self, key, msj):
        self.__mensajes[key] = msj


    def __delitem__(self, key):
        del self.__sprites[key]


