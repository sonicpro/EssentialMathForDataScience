# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:48:23 2024

@author: chegn
"""

# One-tailed test for evaluation the result of a drug for cold test.
# Sample group showed the average recovery of 16 days. Is the drug effective?
from scipy.stats import norm
# Using the inverse cdf to find x-value for the right threshold of p-value of 5%.
sample_mean_for_successful_trial = norm.ppf(0.05, loc=18, scale=1.5)
print(sample_mean_for_successful_trial)
# Prints 15.53271955957279. The trial was unsuccessful. The sample mean
# must be 15.53 days or less.