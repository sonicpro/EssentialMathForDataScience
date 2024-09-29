# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:33:23 2024

@author: chegn
"""

# Three exams of weight 0.20 each and final exam of 0.40 weight.
sample = [90, 80, 63, 87]
weights = [.20, .20, .20, .40]

weighted_mean = sum(s * w for s, w in zip(sample, weights)) / \
    sum(weights)
    
print(weighted_mean) # prints 81.4