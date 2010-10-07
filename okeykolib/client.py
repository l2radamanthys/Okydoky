#!/usr/bin/env python
# -*- coding: utf-8 -*-


from constant import *
from utils import get_response


class OkeykoClient:
    def __init__(self, user="", pswr=""):
        self.__user = ""
        self.__pswr = ""
        self.__cokies = None
        self.__conec_status = False #estado de la conecion

        if user != "" and pswr != "":
            self.login(user, pswr)


    def login(self, user="", pswr=''):
        pass


    def disconect(self):
        pass


    def set_cokie(self):
        pass


    def conection_status(self):
        pass


    def send_oky(self, dest="@", txt=""):
        pass


    def e(self)



