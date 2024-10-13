# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:57:53 2024

@author: chegn
"""

# Example 3-16. Defining the critical_z_value function.

# The function returns the z-value (z-score) that is the x-value of
# a standard normal distribution that left the desired size area on the center
# of the distribution graph.

# Remember that the total area under any normal distribution graph is 1
# given that it is a probabilisty distribution.

from scipy.stats import norm

def critical_z_value(p):
    # A normal distribution is standardised, that is
    # the mean is 0 and the std dev is 1.
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    upper_area_plus_left_tail_area = 1 - ((1 - p) / 2.0)
    # Finding z-values that correspond to tha areas
    # using inverse Cumulative Density function (called
    # ppf in Python).
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area_plus_left_tail_area)

print(critical_z_value(p=.95))
# (-1.959963984540054, 1.959963984540054)