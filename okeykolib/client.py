#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constant import *
from utils import get_response


class OkeykoClient:
    def __init__(self, user="", pswr=""):
        self.__user = user
        self.__pswr = pswr
        self.__cokies = None
        self.__conec_status = False #estado de la conecion

        if user != "" and pswr != "":
            self.connecting(user, pswr)


    def connecting(self, user="", pswr=''):
        """
            iniciar conecion con el servidor
        """
        pass


    def disconnect(self):
        """
            terminar conecion
        """
        pass


    def set_cokie(self):
        pass


    def conection_status(self):
        """
            Estado de la conecion
        """
        pass


    def send_oky(self, dest="@", txt=""):
        """
            Enviar un Oky
        """
        pass


    def send_foky(self, c_area="", num_cel=""):
        """
            Enviar un msj de texto a un numero no perteneciente a Okeyko
        """
        #esta parte esta a prueba todavia no se si se implementara o no
        pass


    def mark_read(self, oky_id=""):
        """
            Marcar mensaje como leido
        """
        pass



    def get_messages(self):
        """
            obtener el listado de todos los mensajes recibidos
        """
        pass


    def get_new_messages(self):
        """
            obtener el listado de todos los mensajes nuevos
        """
        pass


    def get_messages_sent(self):
        """
            obtener el listado de todos los mensajes enviados
        """
        pass


    def get_favorites(self):
        """
            devuelve todos los mensajes marcados como faboritos o importantes
        """
        pass





