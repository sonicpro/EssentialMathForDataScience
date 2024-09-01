# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 18:16:51 2024

@author: chegn
"""

# This is the same approximation of the f(x) = 1 + x**2 integral
# as in Ex.1.26, but using "limit" from SymPy we get the accurate
# value of the integral.

from sympy import symbols, limit, Sum, oo

x, i, n = symbols('x i n')

# Here is the function to integrate:
f = x**2 + 1
# Integrate on the interval [lower, upper].
lower, upper = 0, 1

# The width of each rectangle:
delta_x = (upper - lower) / n
# This is the right edge x coordinage of a rectangle i:
x_i = (lower + delta_x * i)
# This is the height of the rectangle i:
fx_i = f.subs(x, x_i)

# Calculate the total area under the curve.
# Notice that we do not substitute the upper bound of "i" substitution.
area = Sum(delta_x * fx_i, (i, 1, n)).doit()

# Calculate the accurate integral value by using a limit to infinity.
exact_area = limit(area, n, oo)

print(exact_area) # print 4/3