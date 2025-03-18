# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:38:38 2025

@author: arthu
"""

import socket
import struct
import datetime

UDP_IP = "192.168.1.7"
UDP_PORT = 52002
format = 'diiiiffff' # byte array format : d for double , i for int, f for float
sock = socket.socket(socket.AF_INET, # Internet
 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
 data, addr = sock.recvfrom(40) # buffer size is 1024 bytes
 decoded = struct.unpack(format,data)
 print("---------------------------------")
 print("Date : ",datetime.datetime.fromtimestamp(decoded[0]))
 print("Pitch : ",decoded[1])
 print("Roll :",decoded[2])
 print("Yaw :",decoded[3])
 print("Batterie :",decoded[4])
 print("Barometer :",decoded[5])
 print("Agx :",decoded[6])
 print("Agy :",decoded[7])
 print("Agz :",decoded[8])
 print("---------------------------------")