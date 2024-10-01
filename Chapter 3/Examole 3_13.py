# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:02:12 2024

@author: chegn
"""

# Generating a population from a norman distribution.
# The standard distribution is defined by the mean and
# the standard deviation.

# We use a reverse CDF function to get a realistic
# weight for each of 1000 imagined retrievers.

import random
from scipy.stats import norm

mean = 64.43
std_dev = 2.99

for i in range(0, 1000):
    random_p = random.uniform(0.0, 1.0) # the probability that we look for a weight for
    random_weight = norm.ppf(random_p, mean, std_dev)
    print(random_weight)