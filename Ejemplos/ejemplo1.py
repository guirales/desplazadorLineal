#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:39:56 2021

@author: memo
"""

#import time
import desplazadorL as dp
pts=dp.detectar()

desp1,info1=dp.abrirpuertos(pts[0])

dp.mover(desp1,modo="p",cantidad=2000,rapidez=70,sentido=1)##unidades en mm

dp.cero(desp1)


desp1.close()
