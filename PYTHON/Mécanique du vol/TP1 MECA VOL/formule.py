# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:15:32 2025

@author: arthu
"""

from variable import *
from math import *

def q_bar():
    return (1/2 * rho * (U0 ** 2))

def xu():
    qb = q_bar()
    return (((- qb * S) / (m * U0)) * (2 * CD0 + CDu))

def xw():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * (CL0 * (1 - (2 * CLalpha) / (pi * e * A)))

def xdeltat():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * CDdeltat

def xdeltae():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * CDdeltae

def yv():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * Cybeta

def yp():
    qb = q_bar()
    return ((qb * S) / (2 * m * U0)) * Cyp

def yr():
    qb = q_bar()
    return ((qb * S) / (2 * m * U0)) * Cyr

def ydeltar():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * Cydeltar

def ydeltaa():
    qb = q_bar()
    return ((qb * S) / (2 * m * U0)) * Cydeltaa

def zu():
    qb = q_bar()
    return (((qb * S) / (m * U0)) * (2 * CL0 + CLu))

def zw():
    qb = q_bar()
    return (((qb * S) / (m * U0)) * (CD0 + CLalpha))

def zwp():
    qb = q_bar()
    return (((qb * S * c_bar) / (2 * m * U0 ** 2)) * (CD0 + CLalpha))

def zq():
    qb = q_bar()
    return (((qb * S * c_bar) / (2 * m * U0)) * (CLq))

def zdeltat():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * CLdeltat

def zdeltae():
    qb = q_bar()
    return ((qb * S) / (m * U0)) * CLdeltae

def mu():
    qb = q_bar()
    return ((qb * S * c_bar) / (I[1,1] * U0)) * Cmalpha

def mw():
    qb = q_bar()
    return ((qb * S * c_bar) / (I[1,1] * U0)) *  Cmalpha

def mwp():
    qb = q_bar()
    return ((qb * S * c_bar ** 2) / (2 * I[1,1] * U0 ** 2)) * Cmalphap

def mq():
    qb = q_bar()
    return ((qb * S * c_bar ** 2) / (2 * I[1,1] * U0)) * Cmq

def mdeltat():
    qb = q_bar()
    return ((qb * S * c_bar) / (I[1,1] * U0)) * CLdeltat

def mdeltae():
    qb = q_bar()
    return ((qb * S * c_bar) / (I[1,1] * U0)) * Cmdeltae

def lv():
    qb = q_bar()
    return ((qb * S * b) / (I[0,0] * U0)) * Clbeta

def lp():
    qb = q_bar()
    return ((qb * S * b ** 2) / (2 * I[0,0] * U0)) * Clp

def lr():
    qb = q_bar()
    return ((qb * S * b ** 2) / (2 * I[0,0] * U0)) * Clr

def ldeltar():
    qb = q_bar()
    return ((qb * S * b) / (I[0,0] * U0)) * Cldeltar

def ldeltaa():
    qb = q_bar()
    return ((qb * S * b) / (I[0, 0] * U0)) * Cldeltaa

def nv():
    qb = q_bar()
    return ((qb * S * b) / (I[2,2] * U0)) * Cnbeta

def np():
    qb = q_bar()
    return ((qb * S * b ** 2) / (2 * I[2,2] * U0)) * Cnp

def nr():
    qb = q_bar()
    return ((qb * S * b ** 2) / (2 * I[2,2] * U0)) * Cnr

def ndeltar():
    qb = q_bar()
    return ((qb * S * b) / (I[2, 2] * U0)) * Cndeltar

def ndeltaa():
    qb = q_bar()
    return ((qb * S * b) / (I[2, 2] * U0)) * Cndeltaa

def omega(l1,l2):
    return sqrt(l1 * l2)

def ksi(l1,l2):
    om = omega(l1, l2)
    return (- (l1 + l2) / 2 * om)