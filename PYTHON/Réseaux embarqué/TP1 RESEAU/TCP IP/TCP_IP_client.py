# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:41:57 2025

@author: arthu
"""

import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024
sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sconn.bind((TCP_IP, TCP_PORT))
sconn.listen(1)
s, addr = sconn.accept()
rawdata = s.recv(BUFFER_SIZE)
print("received data:", rawdata.decode('ascii'))
print('Client connected with address:', addr)
print('connecting to '+ TCP_IP + ':' + str(TCP_PORT) +'...')
s.send(rawdata) # echo
s.close()
sconn.close()