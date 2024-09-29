# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:16:02 2024

@author: chegn
"""

# Calculating standard deviation.
# Standard deviation is a square root from variance.

from math import sqrt

# Number of pets each person owns.
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values):
    mean = sum(values) / len(values)
    _variance = sum([(v - mean) ** 2 for v in values]) / \
        len(values)
    return _variance

def std_dev(values):
    return sqrt(variance(values))

print(std_dev(data)) # prints 4.624689730353899.