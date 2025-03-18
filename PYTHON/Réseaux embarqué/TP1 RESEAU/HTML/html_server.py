# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:58:29 2025

@author: arthu
"""

import time
import socket

def server():
    http_head = "HTTP/1.1 200 OK\r\n"
    http_head += "Date:"+ time.asctime() +"GMT\r\n"
    http_head += "Expires: -1\r\n"
    http_head += "Cache-Control: private, max-age=0\r\n"
    http_head += "Content-Type: text/html;"
    http_head += "charset=utf-8\r\n"
    http_head += "\r\n"
    data = "<html><head><meta charset='utf-8'/></head>"
    data += "<body><h1>ZE PARTI </h1>"
    data += "</body></html>\r\n"
    data += "\r\n"
    http_response = http_head.encode("ascii") + data.encode("utf-8")
    return http_response


TCP_IP = '127.0.0.1'
TCP_PORT = 55000
BUFFER_SIZE = 1024
sconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sconn.bind((TCP_IP, TCP_PORT))
sconn.listen(1)
s, addr = sconn.accept()
rawdata = s.recv(BUFFER_SIZE)
print("received data:", rawdata.decode('ascii'))
s.send(server()) # echo
s.close()
sconn.close()s

