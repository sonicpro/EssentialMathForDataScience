# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:44:55 2024

@author: chegn
"""

# "Probability of Z-phone lasting from 20 to 30 month".
from scipy.stats import norm

mean = 42.0
std_dev = 8.0

# Area from -oo to 30:
probability_of_lasting_time_up_to_30 = norm.cdf(30.0, loc=mean, scale=8.0)
#Area from -oo to 20:
probability_of_lasting_time_up_to_20 = norm.cdf(20.0, loc=mean, scale=8.0)
print \
    ("A random Z-phone lasts from 20 to 30 months with {} probability.".format(\
        probability_of_lasting_time_up_to_30 - probability_of_lasting_time_up_to_20))