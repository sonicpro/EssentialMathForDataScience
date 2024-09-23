# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:24:15 2024

@author: chegn
"""

# Trying to be more precise with the engine reliability
# value, we increased the number of test trials from
# 10 to 36. We got 30 successes and 6 failures.

# Unfortunately the probability that out engine is 
# 90% or more reliable decreases from 22.5% to
# 13.16% when we increased the number of trials from
# 10 to 36.

successes = 30
failures = 6

# CDF stands for "cumulative distribution function"
from scipy.stats import beta

p = 1.0 - beta.cdf(0.90, successes, failures)

# The probability of having the success probability
# > 90% is 22.5 %.

print(p)