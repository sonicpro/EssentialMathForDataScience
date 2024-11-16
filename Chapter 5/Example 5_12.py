# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:31:00 2024

@author: chegn
"""

# Example 5_12. Printing "Sum of square loss" function.
from sympy import *
from sympy.plotting import plot3d
import pandas as pd

# Read the data
points = list(pd.read_csv('https://bit.ly/3goOAnt').itertuples())

m, b, i, n = symbols('m b i n')
# x and y are function-like symbols. They read values for i point as x(i), y(i).
x, y = symbols('x y', cls=Function)

sum_of_squares = Sum((m * x(i) + b - y(i)) ** 2, (i, 0, n)) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)
    
plot3d(sum_of_squares)