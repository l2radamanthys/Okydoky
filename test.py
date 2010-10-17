#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Autor: Ricardo D. Quiroga -> L2Radamanthys
    licencia: GPL2
    Email: l2radamanthys@gmail.com, ricardoquiroga.dev@gmail.com
    Web: http://www.l2radamanthys.com.ar
"""

from okeykolib.client import OkeykoClient


def main():
    c = OkeykoClient()
    e,m = c.login("test_user", "test_user")
    print c.send_oky("l2radamanthys", "mensaje de prueba")
    #c.logout()


if __name__ == '__main__':
    main()
