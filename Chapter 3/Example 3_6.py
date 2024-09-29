# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:02:22 2024

@author: chegn
"""

# Example 3_6. Population variance.

# Population variance is the mean of squared differences
# between a value and the population mean.

# I call seven people "population" because it is my staff.
# Number of pets each person owns.
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum([(v - mean) ** 2 for v in values]) / \
        len(values)
    return _variance

print(variance(data)) # prints 21.387755102040817.