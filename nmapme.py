#!/usr/bin/env python
# Name:     nmapme
# Purpose:  Python to scan your public IP wihth NMAP (Top 100 ports, Service ID,  Open)
# By:       Jerry Gamblin
# Date:     13.05.15
# Modified  13.05.15
# Rev Level 0.1
# -----------------------------------------------

import urllib2
import subprocess
import sys
import socket
from urllib2 import urlopen

def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)


def red(text):
    return color(text, 31)

def blue(text):
    return color(text, 34)


my_ip = urlopen('http://icanhazip.com').read()
HOST="root@cloud.yoursite.com"

print '\n'
print (red('This is probally illegal. Dont Be Stupid.'))
print '\n'
print 'Scanning ' + my_ip  + ' with namp from ' + HOST
print '\n'

COMMAND="nmap -F -sV --open %s" % my_ip 


ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.read()
if result == []:
    error = ssh.stderr.read()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
