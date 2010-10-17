#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
from constant import *
from utils import *
from excepciones import *

class OkeykoClient:
    def __init__(self, user="", pswr=""):
        self.__user = user
        self.__pswr = pswr
        self.__cokies = None
        self.__conec_status = False #estado de la conecion


    def set_cokies(self):
        if self.__user != "" and self.__pswr != "":
            dict = {
                'usuario': self.__user,
                'clave': self.__pswr,
                'signin_submit': 'Inicio',
                'remember_me': '1'
            }
            params = urllib.urlencode(dict)
            response = get_response(LOGIN_URL, params, True, None, True, True)
            self.__cookies = response.getheader("set-cookie")
            data = response.read()
            response.close()

            pos = data.find("Has iniciado")
            if pos != -1:
                self.__conec_status = True
                return True, data.split("\n")[0][pos:]
            else:
                self.__conec_status = False
                return False, "Password o Usuario incorrecto"
                #raise LoginError(self.__user, self.__pswr)

        else:
            raise LoginError(self.__user, self.__pswr)
            self.__conec_status = False


    def login(self, user="", pswr=''):
        """
            iniciar conecion con el servidor
        """
        if not(self.conection_status()):
            self.__user = user
            self.__pswr = pswr
            if self.__user != "" and self.__pswr != "":
                return self.set_cokies()
            else:
                raise ParamError()


    def logout(self):
        """
            terminar conecion
        """
        pass


    def get_url_data(self, url):
        #equivalente a pagina() en la version original
        if self.__conec_status:
            response = get_response(url=url, cookie=self.__cokies)
            data = response.read()
            response.close()
            return data
        else:
            raise ConectionError()


    def conection_status(self):
        """
            Estado de la conecion
        """
        return self.__conec_status


    def send_oky(self, dest="@", txt=""):
        """
            Enviar un Oky
        """
        if self.__conec_status:
            dest = dest.replace("@", "")#destinatario
            txt = unicode( txt, "utf-8").encode("iso-8859-1")
            if len(txt) > 250: #pronto implement msj multipart
                return False, "la longitud del Mensaje Excede los 250 caracteres"
            else:
                dict = {
                    'para': dest,
                    'message1': txt,
                    'Submit': 'Enviar Oky'
                }
                params = urllib.urlencode(dict)
                response = get_response(SEND_OKY, params, True, self.__cookies, True, True)
                #data = response.read()
                #data_log(data, True)



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






