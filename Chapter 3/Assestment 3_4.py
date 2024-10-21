# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:12:43 2024

@author: chegn
"""

# Calculate p-value for a probability that after the advertising compaign the 
# average sales per day is either >= $11,641 or <= ($10,345 - ($11,641 - $10,345)).

from scipy.stats import norm
mean = 10345.0
std_dev = 552.0

sales_normal_distribution = norm(loc=mean, scale=std_dev)

# Probability of $11,641 or more (upper taild of the normal distribution).
p1 = 1.0 - sales_normal_distribution.cdf(11641.0)
# Probability of sales compaign caused an adverse effect on sales (lower tail of dist.).
p2 = sales_normal_distribution.cdf(10345.0 - (11641.0 - 10345.0))

# P-value of both tails.
p_value = p1 + p2

print(p_value) # 0.018883335964961383 < 0.05

# We consider the advertising compaign successful, because the sales increase
# by $11,641 - $10,345 = $1,296 was enough to produce the p_value <= 0.05.

print("Two-tailed P-value", p_value)
if p_value <= 0.05:
    print("Passes two-tailed test.")
else:
    print("Fails two-tailed test.")