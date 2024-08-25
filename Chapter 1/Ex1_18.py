# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:40:14 2024

@author: chegn
"""

from sympy import symbols, diff

# Declare 'x' to SymPy.
x = symbols('x')

# Declare a (mathematical) function.
f = x**2


# Calculate the derivative of the function.
dx_f = diff(f)
print(dx_f) # prints 2*x