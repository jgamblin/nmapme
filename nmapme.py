#!/usr/bin/env python
# Name:     nmapme
# Purpose:  Python to scan your public IP wihth NMAP 
# By:       Jerry Gamblin
# Date:     13.05.15
# Modified  15.05.15
# Rev Level 0.5
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
HOST="root@yourcloud"

print '\n'
print (red('This is probally illegal. Dont Be Stupid.'))
print '\n'
print 'You are going to Scan ' + my_ip  + ' with namp from ' + HOST
print '\n'

q=input(blue("\nScan Types: \
              \n1. Regular Scan (nmap)\
              \n2. Quick Scan (nmap -T4 -F)\
              \n3. Quick Scan Plus (nmap -sV -T4 -O -F --version-light)\
              \n4. Intense Scan (nmap -T4 -A -v)\
              \n5. Intense Scan Plus UDP (nmap -sS -sU -T4 -A -v)\
              \n6. Intense Scan Plus all TCP (nmap -p 1-65535 -T4 -A -v)\
              \n7. Slow comprehensive scan \n   (nmap -sS -sU -T4 -A -v -PE -PS80,443 -PA3389 -PP -PU40125 -PY --source-port 53)\
              \n\nWhich one do you want to run?:"))

if q == 1:
        COMMAND="sudo nmap %s" % my_ip 
elif q == 2:
        COMMAND="sudo nmap -T4 -F %s" % my_ip 
elif q == 3:
        COMMAND="sudo nmap -sV -T4 -O -F --version-light %s" % my_ip 
elif q == 4:
        COMMAND="sudo nnmap -T4 -A -v %s" % my_ip 
elif q == 5:
        COMMAND="sudo nnmap -sS -sU -T4 -A -v %s" % my_ip 
elif q == 6:
        COMMAND="sudo nmap -sS -sU -T4 -A -v %s" % my_ip 
elif q == 7:
        COMMAND="sudo nmap -sS -sU -T4 -A -v -PE -PS80,443 -PA3389 -PP -PU40125 -PY --source-port 53 %s" % my_ip 
elif q == 42:
        print "\n"
        l33thacker =raw_input(red("I really hope you know what you are doing:"))
        COMMAND = l33thacker
else:
        print("\nUm...that wasnt a choice.")
print('\n')


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
    print "\n"
