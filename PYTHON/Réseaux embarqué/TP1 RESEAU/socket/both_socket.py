# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:18:58 2025

@author: arthu
"""

import select
import socket
import struct
import datetime

UDP_IP = "192.168.1.7"
UDP_PORT1 = 52001
UDP_PORT2 = 52002
format = 'diiiiffff'

sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.bind((UDP_IP, UDP_PORT1))
sock2.bind((UDP_IP,UDP_PORT2))

socketList = [sock1,sock2]

while True:
 ls = select.select(socketList,[],[],1)
 for s in ls[0]:
     data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
     print("#message from:",addr)
     print("#message to :",s.getsockname())
     if(s.getsockname()[1] == UDP_PORT2):
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
     elif(s.getsockname()[1] == UDP_PORT1):
        print("received message:", data.decode('utf8'))
        print("from:",addr)
     
"""
2.1.6 : 52002 port is faster than 52001
"""