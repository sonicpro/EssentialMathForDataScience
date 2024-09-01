# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:42:41 2024

@author: chegn
"""

from sympy import symbols, diff
from sympy.plotting import plot3d

# Declare x and y to SymPy.
x, y = symbols('x y')

# Declare a two-dimensional function.
f = 2 * x ** 3 + 3 * y ** 3

# Calculate the partial derivatives for x and y.
dx_f = diff(f, x)
dy_f = diff(f, y)

print(dx_f)
print(dy_f)

# Plot the function.
plot3d(f)