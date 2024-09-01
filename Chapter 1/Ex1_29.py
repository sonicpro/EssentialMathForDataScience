# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:54:43 2024

@author: chegn
"""

# The same task that in Ex.1.26 but using SymPy.

from sympy import symbols, integrate

x = symbols('x')

# We will integrate the following function:
f = x**2 + 1

# Calculate the integral of the function on an interval 0, 1.
area = integrate(f, (x, 0, 1))
print(area) # It turns out that the integral of f(x) = 1 + x**2
            # is a rational number 4/3.