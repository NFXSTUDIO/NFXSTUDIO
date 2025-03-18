# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:35:01 2025

@author: arthu
"""

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50005
MESSAGE = "Hello, World!"
print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
 socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode('utf8'), (UDP_IP, UDP_PORT))

