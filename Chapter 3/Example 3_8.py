# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:16:02 2024

@author: chegn
"""

# Calculating standard deviation for a sample rather for population.

from math import sqrt

# Number of pets each person owns.
data = [0, 1, 5, 7, 9, 10, 14]

def variance(values, is_sample: bool = False):
    mean = sum(values) / len(values)
    _variance = sum([(v - mean) ** 2 for v in values]) / \
        (len(values) - 1 if is_sample else 0)
    return _variance

def std_dev(values, is_sample: bool = False):
    return sqrt(variance(values, is_sample))

# We increase the variance value comparing to population variance 21.387755
# so as not underestimate the variance of the population
# based on our sample.
print("VARIANCE = {}".format(variance(data, True))) # 24.95238095238095.
print("STD_DEV = {}".format(std_dev(data, True))) # 4.99523582550223.
      