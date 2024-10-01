# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:45:01 2024

@author: chegn
"""

# Finding the probability that a golden retriever has
# a weight less than 64.43 pounds using normal distribution
# function and the corresponding cumulative distribution
# function.

# From the sample we know the standard deviation and
# the mean.

from scipy.stats import norm

mean = 64.43
std_dev = 2.99

# Probability that the weight of a retriever < 64.43 pounds
# is the area under CDF graph
# in a range from zero to 64.43 points.
x = norm.cdf(64.43, mean, std_dev)

print(x) # prints 0.5.