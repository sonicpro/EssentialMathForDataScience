# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:53:18 2024

@author: chegn
"""

# Calculating the possibility to recover from a cold from 15 to 21 day.
# Cold has 18 days mean recovery, 1.5 std dev.
# Recovery time follows normal distribution.

# Using cumulative density function to get the are under the distribution
# curve from -oo to 21 day minus the area from -oo to 15 days.
from scipy.stats import norm

probability = norm.cdf(21.0, loc=18.0, scale=1.5) - \
    norm.cdf(15.0, loc=18.0, scale=1.5)
    
print(probability) # 0.9544997361036416