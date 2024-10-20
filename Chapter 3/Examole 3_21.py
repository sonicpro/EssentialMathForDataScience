# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:47:19 2024

@author: chegn
"""

# Using two-tail testing for evaluating the statistical significance of a 
# drug from cold trial.

# Like in other examples, without a drug the mean recovery time is 18 days,
# std dev 1.5 days.

from scipy.stats import norm

# We divide the p-value of 5% to the left tail of 2.5% probability and the right tail
# of 2.5% probability.

# Calculate the range from -oo to max x-value that is being compared to sample mean
# defines if the drug reduces the recovery time.
left_threshold = norm.ppf(0.025, loc=18.0, scale=1.5)

# The same for the right threshold.
right_threshold = norm.ppf(0.975, loc=18.0, scale=1.5)

print(left_threshold) # 15.060054023189918
print(right_threshold) # 20.93994597681008

# If the clinical trial group showed 16 days average recovery time it's result is
# not significant. Because 16 does not fall in either left tail or right tail.