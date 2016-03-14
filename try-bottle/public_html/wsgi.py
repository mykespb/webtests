#!/usr/bin/env python2
#coding: utf-8

# wsgi.py

import sys, os, bottle

activate_this = '/var/www/tryonce/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/var/www/tryonce/public_html')
sys.path.insert(0, '/var/www/tryonce')
sys.path.insert(0, '/var/www/tryonce/lib/python2.7')
sys.path.insert(0, '/var/www/tryonce/lib/python2.7/site-packages')

os.chdir(os.path.dirname(__file__))

import main

application = bottle.default_app()

