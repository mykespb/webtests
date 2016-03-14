#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# 2014-04-15 4.7. myke: get access to afisha database and print all info from it

from __future__ import division, print_function

import datetime as dt
import os, sys
import string, re

#from bottle import *
from bottle import run, get

__author__  = 'myke'
__version__ = '5.2'
#DATABASE    = 'data/ap.db'

#dtoday = dt.date.today()
#dtoday = dt.datetime.now()
#dout = str(dtoday.isoformat())

def getweekday(s):
    """ weekday from sql string """
    # print (s, s[:10], s.split('-'))
    dd = [int(q) for q in s.split('-')]
    d = datetime.date(*dd)
    # print (d)
    wds = [u"пн", u"вт", u"ср", u"чт", u"пт", u"сб", u"вс"]
    # print (wds)
    return wds[d.weekday()]

def markurls (s):
    t = re.sub (r"(http://[-a-zA-Z0-9,.%()!?/]+)", r"<a href='\1'>\1</a>", s)
    return t

@get('/')
def index():
    """ show all data from database """
#    return template("bdata.html", data=d, dt=dt.datetime.now(), ver=__version__)
    dtoday = dt.datetime.now()
    dout = str(dtoday.isoformat())
    return "Hello from python " + sys.version + " today is " + dout

if __name__ == '__main__':
    run(host='localhost', port=8080)
