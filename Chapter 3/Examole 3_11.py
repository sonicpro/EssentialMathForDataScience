# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:51:21 2024

@author: chegn
"""

# Finding a probability that the weight of a golden
# retriever is between 62 and 66 pounds using normal
# distribution and the corresponding cumulative
# distribution function.

# From the sample we know the standard deviation and
# the mean.

from scipy.stats import norm

mean = 64.43
std_dev = 2.99

# Probability that the weight of a retriever < 64.43 pounds
# is the area under CDF graph
# in a range from zero to 64.43 points.
x = norm.cdf(66, mean, std_dev) - \
norm.cdf(62, mean, std_dev)

print(x) # prints 0.4920450147062894.