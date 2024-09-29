# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:33:23 2024

@author: chegn
"""

# Three exams of weight 0.20 each and final exam of 0.40 weight.
sample = [90, 80, 63, 87]
# The weights does not have to sum up to 100%.
# If the proportion of a score of final exam to the score of a common exam
# is the same, the weighted mean value will be the same.
# weights = [.20, .20, .20, .40]
weights = [1, 1, 1, 2]

weighted_mean = sum([s * w for s, w in zip(sample, weights)]) / \
    sum(weights)
    
print(weighted_mean) # prints 81.4