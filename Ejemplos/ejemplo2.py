#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:26:33 2021

@author: Guillermo Guirales
"""
import time
import desplazadorL as dp
pts=dp.detectar()

desp1,info1=dp.abrirpuertos(pts[0])

for d in range(0,2,1):
    est=dp.mover(desp1,modo="mm",cantidad=50,rapidez=50)##unidades en mm
    time.sleep(2)
    if "FC1" in est:
        break
"""    
for d in range(0,5,1):
    dp.mover(desp1,cantidad=10,rapidez=50,sentido=0)##unidades en mm
    time.sleep(2)
    """
    
dp.cero(desp1)


desp1.close()

