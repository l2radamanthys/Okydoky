#!/usr/bin/env python
# -*- coding: utf-8 -*-


#import urllib
import httplib

from constantes import DOMAIN


def get_response(url='', params=None, ref=False, cookie=None, ctype=False, clength=False):
    """

    """

    headers = NAV_HEADERS.copy()

    if ref:
        headers["Referer"] = DOMAIN + "/default.php"
    if cookie:
        headers["Cookie"] = cookie
    if ctype:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if clength:
        headers["Content-Length"] = len(params)

    connection = httplib.HTTPConnection(DOMAIN, 80)
    if params:
        connection.request("POST", url, params, headers)
    else:
        connection.request("GET", url, params, headers)

    return connection.getresponse()


def changeEntities(str):
    str = str.encode( "utf-8" )
    lst = htmlentitydefs.name2codepoint
    for find, replace in lst.iteritems():
        find = "&%s;" % (find)
        replace = unichr(int(replace))
        #replace = "&%s;" % (replace)
        str = str.replace(find, replace)
    return str


def toEntities(str):
    print "pre %s" % (str)
    #lst = htmlentitydefs.codepoint2name
    #for find, replace in lst.iteritems():
        #replace = "&#%s;" % (find)
        #replace = "&%s;" % (replace)
        #find = unichr(int(find))
        #str = str.replace(find, replace)
    #str = unicode(str, "iso-8859-1")
    #str = unicode(str, "utf-8")
    #print "pos %s" % (str)
    return str
