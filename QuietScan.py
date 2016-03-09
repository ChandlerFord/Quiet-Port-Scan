__author__ = 'Chandler'

from logging import getLogger, ERROR
import sys
from datetime import datetime
from time import strftime

try:
    from scapy.all import *
except Exception:
    print 'Scapy Not Installed!'
    sys.exit(1)

getLogger("scapy.runtime").setlevel(ERROR)

try:
    target = raw_input("Target IP: ")
    min_port = raw_input("Enter Minimum Port: ")
    max_port = raw_input("Enter Maximum Port: ")
    try:
        if int(min_port) >= 0 and int(max_port) > 0 and int(max_port) >= int(min_port):
            pass
        else:
            print '\nInvalid Range of Ports'
            sys.exit(1)
    except Exception:
        print '\nInvalid Range of Ports'
        sys.exit(1)
except KeyboardInterrupt:
    print 'Interrupted by User!'
    sys.exit(1)
