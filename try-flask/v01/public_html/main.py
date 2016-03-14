#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# 2016-03-15 6.2
# myke. test access to flask from venv, py2

from __future__ import division, print_function

import datetime as dt
import os, sys
import string, re

from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    dtoday = dt.datetime.now()
    dout = str(dtoday.isoformat())
    return "Hello from flask " + sys.version + " today is " + dout

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
