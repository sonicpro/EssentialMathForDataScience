# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:09:26 2024

@author: chegn
"""
from scipy.stats import norm

def crit_z_values(p):
    #Using standard normal distribution, expecting the lower_crit_z is negative
    std_norm_dist = norm(loc=0.0, scale=1.0)
    # Dividing the given probability by 2 and put the areas to the lower end of
    # the distribution and to the upper end of it:
    lower_crit_z = std_norm_dist.ppf((1.0 - p) / 2.0)
    upper_crit_z = std_norm_dist.ppf(1.0 - ((1.0 - p) / 2.0))
    return lower_crit_z, upper_crit_z

from math import sqrt

def confidence_interval(p, sample_mean, sample_size, sample_std):
    # To calculate "Error margin" we do not use sample_mean, just use crit. z-values
    # by the formula.
    # Left marging expected to be nagative. lower_crit_z from crit_z_values is negative.
    lower_crit_z, upper_crit_z = crit_z_values(p)
    left_margin = lower_crit_z * sample_std / (sqrt(sample_size))
    right_margin = upper_crit_z * sample_std / (sqrt(sample_size))
    return sample_mean + left_margin, sample_mean + right_margin

print(\
"The diameter of the filament is between {} and {} with 99% confidence".format(\
    *confidence_interval(0.99, 1.715588, 34, 0.029252)))