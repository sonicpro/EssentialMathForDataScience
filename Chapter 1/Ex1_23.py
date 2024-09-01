# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:55:11 2024

@author: chegn
"""

# Ex. 1.23. Using limits to calculate a derivative.
from sympy import symbols, limit

# "x" and step size "s".
x, s = symbols('x s')

# Declare the function.
f = x ** 2

# Substitute x with x + s in the function.
f_1 = f.subs(x, x + s)

# The numerator is the rise of the slope.
# The denominator is the run of the slope.
slope_f = (f_1 - f) / ((x + s) - x)

# Calculate derivative function.
dx_f = limit(slope_f, s, 0)

print(dx_f)

