# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:20:09 2024

@author: chegn
"""

# Calculating the odds that given a test series of
# ten tests with 8 successes and two failures
# the underlying probability of a successful test
# is > than 90%.

successes = 8
failures = 2

# CDF stands for "cumulative distribution function"
from scipy.stats import beta

p = 1.0 - beta.cdf(0.90, successes, failures)

# The probability of having the success probability
# > 90% is 22.5 %.

print(p)