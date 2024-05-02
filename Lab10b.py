#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:27:40 2024

@author: reggiehacker
"""

import numpy as np
from scipy.integrate import quad

#define function to be integrated
def f(x):
    return np.exp((-x**2)/2)

#Integrate function from 0 to 5
result, error = quad(f, 0, 5)

print("integral: ", result)
print("Estimated Error: ", error)

#checking an integral calculator online, this seems to be pretty spot on