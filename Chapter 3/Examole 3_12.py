# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:56:53 2024

@author: chegn
"""

# Using the inverse cumulative distribution function.
# It is called PPF in scipy.

# What weight should have a retriever so that is falls
# under 95% of all retrievers?

from scipy.stats import norm

mean = 64.43
std_dev = 2.99

x = norm.ppf(.95, mean, std_dev)

print(x) # 69.3481123445849 pounds