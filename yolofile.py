# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:50:32 2022

@author: Dapwner
"""

import numpy as np

x=np.zeros((10,2))
y=x+2

z=y[0:4,0]
z=z+z+2+1
print(z)
