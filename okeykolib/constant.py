#!/usr/bin/env python
# -*- coding: utf-8 -*-

DOMAIN = "www.okeyko.com"
LOGIN_URL = "/nv02/validar_usuario.php"
BUSCA_FILTRADO = "/busca_filtrado.php"
SEND_OKY = "/nv02/upd_mensaje.php"


NAV_HEADERS = {
    #"User-Agent": "Mozilla/5.0 (compatible) Cliente Okeyko - Okydoky (Alpha Version)",
    "User-Agent": "Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.1.9) Gecko/20100401 Ubuntu/9.10 (karmic) Firefox/3.5.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-ar,es;q=0.8,en-us;q=0.5,en;q=0.3",
    "Accept-Charset": "utf-8,ISO-8859-1;q=0.7,*;q=0.7",
    "Keep-Alive": "300",
    "Proxy-Connection": "keep-alive",
}

