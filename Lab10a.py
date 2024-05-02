#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:35:42 2024

@author: reggiehacker
"""

from scipy.integrate import quad

#define function to be integrated
def f(x):
    return x**2

#Integrate function from 0 to 2
result, error = quad(f, 0, 2)

print("integral: ", result)
print("Estimated Error: ", error)

#doing this by hand, (and general knowledge of integrals), I got the same exact result