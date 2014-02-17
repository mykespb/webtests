abtests
=======

Make ab (apache benchmark) web sites tests.

Usage:
------

    mk-ab-tests.py [ADDR... | -f FILE] [-t TIMES] [-c CONC] [-p PATH]
    mk-ab-tests.py -h | --help
    mk-ab-tests.py -v | --version

Options:
--------

    -t TIMES      times to run test [default: 100]
    -c CONC       concurrent requests [default: 10]
    -p PATH       path to ab routine [default: ab]
    -f FILE       file with list of addresses (whitespaces separated)
    -v --version  program version
    -h --help     this help page

Arguments:
----------

    ADDR    address[es] to be tested
  
Examples:
---------

    mk-ab-tests.py addr1
      test addr1 100 times with concurrence 10 with ab 
    mk-ab-tests.py addr1 addr2 addr3
      test addr1, addr2, addr3
    mk-ab-tests.py addr1 -t 200 -c 25
      test addr1 200 times with concurrency 25
    mk-ab-tests.py addr1 -t 100,200,300 -c 10,20,30
      test addr1 with each set of times: 100, 200, 300 and
      concurrency 10, 20 and 30   
    mk-ab-tests.py -f list.txt
      text all files from file list.txt with usual parameters
      