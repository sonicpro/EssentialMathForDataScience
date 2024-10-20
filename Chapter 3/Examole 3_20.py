# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:24:15 2024

@author: chegn
"""

# Another way to perform One-tailed test for hyposesis tesing.
# We will calculate the area under normal distribution function
# from -oo to the mean recovery time of the cold drug clinical trial group.
from scipy.stats import norm

p_value = norm.cdf(x=16.0, loc=18.0, scale=1.5)
print(p_value) # prints 0.09121121, the maximum p-value for the successful trial
# is <= 0.05.