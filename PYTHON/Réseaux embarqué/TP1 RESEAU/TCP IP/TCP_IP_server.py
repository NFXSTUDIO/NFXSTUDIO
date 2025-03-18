# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:36:39 2025

@author: arthu
"""

""" 
    Question :

        1) Cet adresse permet a l'ordinateur de communiquer avec lui même
        2) Le premier fichier est le reciever (client), le second le sender (server)
        3) Il y a deux socket car le serveur veut vérifier que le message à été envoyé

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
