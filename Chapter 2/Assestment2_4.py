# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:20:40 2024

@author: chegn
"""

from scipy.stats import binom

k = 50
n = 137
p = .40

probability_of_50_empty_seats = 0.0
# Start from binom.pmf(50, 137, 0.4) probability
# then add up the rest passengers probability of
# them not show up by changing the number of "successes"
# by one for each of the passengers above 50.
for k_prime in range(k, n + 1):
    probability_of_50_empty_seats += binom.pmf(k_prime, n, p)

print(probability_of_50_empty_seats)