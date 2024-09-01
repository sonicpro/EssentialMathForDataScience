# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:23:13 2024

@author: chegn
"""

# Example 1.26. The first try to approximate an area under a curve.

# Defining a function that calculates an approximate area under
# function's f curve on an [a, b] interval. "n" argument is a 
# number of rectangles we divide the area to.
def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_rectangle_height_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_rectangle_height_sum += f(midpoint)
        
    return total_rectangle_height_sum * delta_x

# Let's calculate an approximate integral of f = 1 + x**2 function.
def my_function(x):
    return x**2 + 1

area = approximate_integral(0, 1, 5, my_function)
print(area) #prints 1.33

area_with_more_precision = approximate_integral(0, 1, 1_000_000, my_function)
print(area_with_more_precision)