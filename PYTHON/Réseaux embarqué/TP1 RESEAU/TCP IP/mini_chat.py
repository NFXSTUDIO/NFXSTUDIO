# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:54:19 2025

@author: arthu
"""

import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024 # read size
msg = "Hello, Everyone!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print("Waiting client ...")
print("binding to "+ TCP_IP +":"+str(TCP_PORT)," ...")
s.send(msg.encode('ascii'))
print('sending data...')
rawdata = s.recv(BUFFER_SIZE)
print("received data:\n", rawdata.decode('ascii'))
s.close()