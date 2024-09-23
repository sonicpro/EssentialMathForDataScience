# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 11:35:57 2024

@author: chegn
"""

# Binomial distribution.
from scipy.stats import binom

# Number of trials.
n = 10
# Probability of success in a trial.
p = 0.9

# Getting the number of successes in k trials.
for k in range(n + 1):
    # pmf stands for "probability mass function"
    probability = binom.pmf(k, n, p)
    print("{0} - {1}".format(k, probability))