# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:11:37 2024

@author: chegn
"""

# Example 5_11 solving linear regression using SymPy
import pandas as pd
from sympy import *

# Read the data
points = list(pd.read_csv('https://bit.ly/3goOAnt').itertuples())

m, b, i, n = symbols('m b i n')
# x and y are function-like symbols. They read values for i point as x(i), y(i).
x, y = symbols('x y', cls=Function)

# Function we will calculate partial derivatives for:
sum_of_squares = Sum((m * x(i) + b - y(i)) ** 2, (i, 0, n))

# Calculating d/dm(sum_of_squares). Substitute n for the index of the last point.
# Substitute x and y by anonymous functions.
d_m = diff(sum_of_squares, m) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)
# Calculate d/db(sum_of_squares).
d_b = diff(sum_of_squares, b) \
    .subs(n, len(points) - 1).doit() \
    .replace(x, lambda i: points[i].x) \
    .replace(y, lambda i: points[i].y)
    
# Convert d_m and d_b SymPy expressions to functions.
d_m = lambdify([m, b], d_m)
d_b = lambdify([m, b], d_b)
    
# Building the model.
m = 0.0
b = 0.0

# The Learning Rate
L = .001

# The number of iterations.
iterations = 100_000

# Perform Gradient Descent
for i in range(iterations):
    # update m and b proportionally to the last computed partial derivative value.
    m -= d_m(m, b) * L
    b -= d_b(m, b) * L
    
print("y = {0} * x + {1}".format(m, b))
# y = 1.939393939393954 * x + 4.733333333333231