#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dinntec
"""
import time
import desplazadorL as dp
pts=dp.detectar()

desp1,info1=dp.abrirpuertos(pts[0])

dp.mover(desp1,cantidad=150)##unidades en mm
time.sleep(1)
dp.mover(desp1,cantidad=50,sentido=0)#unidades en mm

dp.mover(desp1,cantidad=10,sentido=1)

dp.cero(desp1)


desp1.close()
