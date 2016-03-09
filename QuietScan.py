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

ports = range(int(min_port),int(max_port)+1)
start_timer = datetime.now()

def pinghost(ip):
    #Verbosity set to 0
    conf.verb = 0
    try:
        #Ping target
        ping = sr1(IP(dst=ip)/IMCP())
        print 'Host is live!' + '\nStarting Scan...'
    except Exception:
        print 'Could not reach Host'
        sys.exit(1)

#TCP Flag values
#Connected value
SYNACK = 0x12
#Reset value
RSTACK = 0x14

def portscan(port):
    sourceport = RandShort()
    conf.verb = 0
    SYNACKpkt = srl(IP(dst=target)/TCP(sport=sourceport, dport=port, flags="S"))
    pktflags = SYNACKpkt.getlayer(TCP).flags
    #Checks TCP flag value for connection state
    if pktflags == SYNACK:
        return True
    else:
        return False
    RSTpkt = IP(dst=target)/TCP(sport=sourceport, dport=port, flags="R")
    send(RSTpkt)

pinghost(target)
print 'Scan Started at: ' + strftime("%H:%M:%S:") + '!\n'
for port in ports:
    status = portscan(port)
    if status == True:
        print 'Port ' + port + ': Open'

stop_timer = datetime.now()
total_time = stop_timer - start_timer
print 'Finished Scan!'
print 'Time Elapsed: ' + str(total_time)





