# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:30:25 2024

@author: chegn
"""

# Using "Gradient descent" technique to calculate simlpe linear regression.

import pandas as pd

# Getting data (number of vets visits depending on a dog age).
points = list(pd.read_csv('https://bit.ly/3goOAnt').itertuples())

# m is a slope, b is an intersect.
m = 0.0
b = 0.0

# "Learning rate" for increasing / decreasing m and b proportionally to a value of partial
# derivative by m or b.
L = 0.001

number_of_iterations = 100_000

# Performing "Gradient descent".
# The function from which we take partial derivatives by m and b is the 
# "sum of squares loss function" E(m, b) = SIGMA_i_to_n(y_i - mx_i - b)^2.

# If you forgot the rules of derivation look into "Math" copybook and watch
# https://www.youtube.com/watch?v=StHyJm5xcjs video.

for i in range(number_of_iterations):
    # The value of d/dm(E) for the current m and b:
    D_m = sum(2 * (m * p.x**2 + b * p.x - p.x * p.y) for p in points)
    
    # The value of d/db(E) for the current m and b:
    D_b = sum(2 * (m * p.x + b - p.y) for p in points)
    
    # Adjust m and b according to how big the derivatives are. In a local minimum
    # of E(m, b) function both derivatives should be close to 0.
    m -= L * D_m
    b -= L * D_b
    
print("y = {}*x + {}".format(m, b))
# y = 1.9393939393939548*x + 4.733333333333227


