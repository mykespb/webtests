#!/usr/bin/env python2
#coding: utf-8

# wsgi.py

import sys, os, flask

activate_this = '/var/www/tryflask/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/www/tryflask/public_html')
sys.path.insert(0, '/var/www/tryflask')
sys.path.insert(0, '/var/www/tryflask/lib/python2.7')
sys.path.insert(0, '/var/www/tryflask/lib/python2.7/site-packages')

os.chdir(os.path.dirname(__file__))

#import main

from main import app as application

