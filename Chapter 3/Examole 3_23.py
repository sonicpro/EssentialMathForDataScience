# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:22:43 2024

@author: chegn
"""

# Example 3_23. Getting critical value range with a T-distribution.
# Use this instead of Example 3_16 if you have sample size < 31.

# Get critical value range for %95 confidence with
# a sample size of 25.

# import t instead of norm.
from scipy.stats import t

n = 25

def critical_t_value(p):
    left_area = (1.0 - p) / 2.0
    upper_area_plus_left_area = 1.0 - (1.0 - p) / 2.0
    
    # "df" stands for "degrees of freedom". Just like in the formula for sample
    # variance, we should substract 1 from the sample size to get df.
    lower_t_value = t.ppf(left_area, df=n - 1)
    upper_t_value = t.ppf(upper_area_plus_left_area, df=n - 1)
    return lower_t_value, upper_t_value

print(critical_t_value(0.95))
# (-2.0638985616280205, 2.0638985616280205) the confidence interval is wider
# comparing to Example 3_16 (normal distribution). This reflect the greater
# uncertainty in data values in T-distribution.