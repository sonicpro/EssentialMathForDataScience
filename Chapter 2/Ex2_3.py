# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:05:29 2024

@author: chegn
"""

# Using scipy to find the probability of a certain
# "underlying probability of success". Underlying probability is
# the probability of success given an infinite number of trials.

# Let's find the probability of the case when underlying
# probability is less than 90% and in ten trials we got 2 failures.
successes = 8
failures = 2

# CDF stands for "cumulative dencity function".
from scipy.stats import beta

p = beta.cdf(.90, successes, failures)

# The probability of having < 90% probability is 77.48%:
print(p)