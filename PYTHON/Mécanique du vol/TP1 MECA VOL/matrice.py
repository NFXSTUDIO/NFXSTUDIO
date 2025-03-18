# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:16:03 2025

@author: arthu
"""

import numpy as np1
from variable import *
from formule import *
from math import *


def A_longitudinal():
    A_long = np1.array([[xu(),xw(),0,- g * cos(theta0)],[zu(),zw(),U0,- g * sin(theta0)],[mu() + zu() * mwp(),mw() + zw() * mwp(),mq() + U0 * mwp(),0],[0,0,1,0]])
    return A_long

def B_longitudinal():
    B_long = np1.array([[xdeltae(),xdeltat()],[zdeltae(),zdeltat()],[mdeltae() + zdeltae() * mwp(),mdeltat() + zdeltat() * mwp()],[0,0]])
    return B_long

def A_latteral():
    A_lat = np1.array([[yv(),yp(),(yr() - U0),g * cos(theta0)],[lv(),lp(),lr(),0],[nv(),np(),nr(),0],[0,1,0,0]])
    return A_lat

def B_latteral():
    B_lat = np1.array([[ydeltar(),ydeltaa()],[ldeltar(),ldeltaa()],[ndeltar(),ndeltaa()],[0,0]])
    return B_lat

def all_lambda(A):
    l1,l2,l3,l4 = np1.linalg.eigvals(A)
    return (l1,l2,l3,l4)

l11,l21,l31,l41 = all_lambda(A_longitudinal())
l12,l22,l32,l42 = all_lambda(A_latteral())



print("-------------------------------------------")
print("Longitudinal : ")
print("-------------------------------------------")
print("Matrice de l'avion : ")
print(A_longitudinal())
print("-------------------------------------------")
print("Matrice de controle : ")
print(B_longitudinal())
print("-------------------------------------------")
print("Lambda : ")
print("lambda 1 :",l11)
print("lambda 2 :",l21)
print("lambda 3 :",l31)
print("lambda 4 :",l41)
print("-------------------------------------------")
print("Lateral : ")
print("-------------------------------------------")
print("Matrice de l'avion : ")
print(A_latteral())
print("-------------------------------------------")
print("Matrice de controle : ")
print(B_latteral())
print("-------------------------------------------")
print("Lambda : ")
print("lambda 1 :",l12)
print("lambda 2 :",l22)
print("lambda 3 :",l32)
print("lambda 4 :",l42)
print("-------------------------------------------")




# print("Ksi : ")
# print("Ksi 1 : ",ksi1_lat)
# print("Ksi 2 : ",ksi2_lat)
# print("-------------------------------------------")
# print("Ksi : ")
# print("Ksi 1 : ",ksi1_long)
# print("Ksi 2 : ",ksi2_long)
# print("-------------------------------------------")

# ksi1_long = ksi(l11, l21)
# ksi2_long = ksi(l31,l41)
# ksi1_lat = ksi(l12, l22)
# ksi2_lat = ksi(l32,l42)