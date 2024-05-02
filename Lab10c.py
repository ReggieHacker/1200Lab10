#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:28:57 2024

@author: reggiehacker
"""


import numpy as np
from scipy.integrate import quad

#define function to be integrated
def f(x):
    return np.exp((-x**2)/2)

#Integrate function from -inf to inf
result, error = quad(f, -np.inf, np.inf)

print("integral: ", result)
print("Estimated Error: ", error)

#it does a pretty good job up to about the sixth decimal place, we can also see
#that the error is larger than the other ones we tried