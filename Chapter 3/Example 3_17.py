# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:07:38 2024

@author: chegn
"""
# Example 3_17. Calculating in which range falls
# with the confidence of 95% the mean of golden retrievers
# population weight.
from math import sqrt
from scipy.stats import norm

def critical_z_value(p):
    # A normal distribution is standardised, that is
    # the mean is 0 and the std dev is 1.
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area = (1.0 - p) / 2.0
    upper_area_plus_left_tail_area = 1 - ((1 - p) / 2.0)
    # Finding z-values that correspond to tha areas
    # using inverse Cumulative Density function (called
    # ppf in Python).
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area_plus_left_tail_area)

# Applying the formula for "Error margin" to convert critical z-values
# back to the values based on the sample mean.

def confidence_interval(p, sample_mean, sample_std, n):
    # We expect that sample size n is greater than 30, so the
    # distribution of the sample means resembles a normal distribution.
    lower_critical_z, upper_critical_z = critical_z_value(p)
    lower_error_margin = lower_critical_z * (sample_std / sqrt(n))
    upper_error_margin = upper_critical_z * (sample_std / sqrt(n))
    return sample_mean + lower_error_margin, sample_mean + upper_error_margin

# We have a sample of 31 golden retriever. We measure the mean weight on
# one of 64.408 pounds and the standard deviation of all retriever weights
# is 2.05 pounds. To what interval falls the weight of any golden retriever
# in the world with the 95% degree of confidence?
print(confidence_interval(p=.95, sample_mean=64.408, sample_std=2.05, n=31))
# (63.68635915701992, 65.12964084298008)