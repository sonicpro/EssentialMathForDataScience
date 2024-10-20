# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:24:15 2024

@author: chegn
"""

# Two-tailed test for evaluating the effectiveness of a drug for cold trial
from scipy.stats import norm

# left tail area. 
p_left_area = norm.cdf(x=16.0, loc=18.0, scale=1.5)
# Symmetrical right tail area.
p_right_area = 1.0 - norm.cdf(x=20.0, loc=18.0, scale=1.5)
p_value = p_left_area + p_right_area
print(p_value) # prints 0.18242243945173575, the maximum p-value for the successful trial
# is <= 0.05.
# Out p-value of 18.24% is twice a much comparing to the p-value of one-tail testing in
# Example 3_20.py. Two-tail testing creates a higher significance threshold for evaluating
# the statistical significance of the variable in question.
# "Variable in question" in this example is the fact of taking the drug
# by a clinical trial group.