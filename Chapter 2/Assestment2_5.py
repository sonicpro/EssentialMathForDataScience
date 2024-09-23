# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 18:07:29 2024

@author: chegn
"""

from scipy.stats import beta

number_of_flips = 19
times_got_heads = 15
fair_coin_underlying_probability = .50
# An area under the curve to the left of the .50 probability is the probability
# to get tails from the coin.
probability_to_get_tails = beta.cdf(fair_coin_underlying_probability, 19, 15)

# The whole area under the curve is 1, to the probability to get heads is 1
# minus the probability to get tails.
probability_to_get_heads = 1.0 - probability_to_get_tails

print ("""
Probability to get heads is grater than to ptobability to get tails in
""")
print ("{0} times.".format(probability_to_get_heads / probability_to_get_tails))
print("Coin is probably unfair.")
       