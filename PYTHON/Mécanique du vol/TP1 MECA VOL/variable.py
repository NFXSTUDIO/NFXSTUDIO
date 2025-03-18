# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:14:53 2025

@author: arthu
"""

import numpy as np

S = 34.84 #wing area
b = 11.8 #wing span
A = 4 #aspect ratio
c_bar = 3.29 #mean aerodynamic chord
e = 0.85 #oswald number
g = 9.81 #gravity
m = 9926.7 #mass kg
H = 0 #altitude
rho = 1.225 #air density
U0 = 85 #Flight speed
M = 0.25 #mach number
theta0 = 11.2 #initial pitch angle
CL0 = 0.62 #lift coefficient
CD0 = 0.072 #Drag coefficient

#Longitudinal stability derivates
CDu = 0.0105
CDa = 1.52
CLu = 0.04
CLalpha = 3.95
CLalphap = 0
CLq = 0
Cmu = 0.012
Cmalpha = -0.45
Cmalphap = -0.7
Cmq = -3.8

#Longitudinal control derivatives :
CDdeltae = 0
CLdeltae = 0.6
Cmdeltae = -0.83
CDdeltat = CLdeltat = Cmdeltat = 0

#Lateral stability derivatives :
Cybeta = -0.88
Cyp = 0
Cyr = 0
Clbeta = -0.115
Clp = -0.25
Clr = 0.18
Cnbeta = 0.105
Cnp = -0.01
Cnr = -0.34

#Lateral control derivatives :
Cydeltaa = -0.015
Cldeltaa = 0.055
Cndeltaa = -0.002
Cydeltar = 0.23
Cldeltar = 0.007
Cndeltar = - 0.105

#Inertial matrix :

I = np.array([[18486.6,0,0],[0,68965,0],[3976.6,0,91599]])

