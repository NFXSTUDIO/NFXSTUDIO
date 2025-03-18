# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:32:34 2025

@author: arthu
"""
import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 50005
sock = socket.socket(socket.AF_INET, # Internet
 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
 data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
 print("received message:", data.decode('utf8'))
 print("from:",addr)
