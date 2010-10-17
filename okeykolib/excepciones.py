#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ParamError(Exception):
    def __str__(self):
        return "Error - Parametros invalidos"


class LoginError(Exception):
    """
        Execpcion que es lanzada al fallar el intento de conecion
    """
    def __init__(self, user="", pswr=""):
        self.user = user
        self.pswr = pswr

    def __str__(self):
        return """Error - Usuario inexistentes o campos obligatorios vacios
        - USER: %s
        - PSWR: %s"""%(self.user, self.pswr)

class ConectionError(Exception):
    def __str__(self):
        return "Error - No existe ninguna conecion activa"
