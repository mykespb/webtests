#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  mk-ab-tests.py
#  make local ab tests 
#  
#  Copyright 2014 myke <myke@MK-ASUS>

"""mk-ab-tests.py

Make ab (apache benchmark) web sites tests.

Usage:
  mk-ab-tests.py [ADDR... | -f FILE] [-t TIMES] [-c CONC] [-p PATH]
  mk-ab-tests.py -h | --help
  mk-ab-tests.py -v | --version

Options:
  -t TIMES      times to run test [default: 100]
  -c CONC       concurrent requests [default: 10]
  -p PATH       path to ab routine [default: ab]
  -f FILE       file with list of addresses (whitespaces separated)
  -v --version  program version
  -h --help     this help page

Arguments:
  ADDR    address[es] to be tested
  
Examples:
  mk-ab-tests.py addr1
    test addr1 100 times with concurrence 10 with ab 
  mk-ab-tests.py addr1 addr2 addr3
    test addr1, addr2, addr3
  mk-ab-tests.py addr1 -t 200 -c 25
    test addr1 200 times with concurrency 25
  mk-ab-tests.py addr1 -t 100,200,300 -c 10,20,30
    test addr1 with each set of times: 100, 200, 300 and
    concurrency 10, 20 and 30   

"""

from __future__ import absolute_import, division, print_function
from docopt import docopt
import string, os

__author__  = 'Mikhail (myke) Kolodin'
__version__ = '0.4'
__date__    = '2014-02-17'

print ("This is mk-ab-tests.py ny %s, ver. %s of %s" % (__author__, __version__, __date__))

arg = docopt (__doc__, version = __version__)

def goodname (s, f):
	""" filter goog chars f in string s"""
	ous = ''.join([c for c in s if c in f])
	return ous

def main():
	""" main desc """
#	print (arg)
	times = arg['-t'].split(',') if ',' in arg['-t'] else [arg['-t']]
	concs = arg['-c'].split(',') if ',' in arg['-c'] else [arg['-c']]
	
	if arg['-f']:
		with open(arg['-f']) as f:
			addr = f.read().split()
	else:
		addr = arg['ADDR']
	
	for addr in addr:
		for c in concs:
			for t in times:
				fname = goodname(addr, string.ascii_letters + string.digits)
				fname += '_t' + t + '_c' + c + '.report'
#				print (fname)
				cmd = arg['-p'] + ' -n ' + t + ' -c ' + c + ' ' + addr + ' > ' + fname
				print (cmd)
				os.system (cmd)
	
	return 0

if __name__ == '__main__':
	main()

