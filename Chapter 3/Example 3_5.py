# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:50:52 2024

@author: chegn
"""

from collections import defaultdict

# Example 3_5. Calculating the mode of population or sample.

# Number of pets each person owns.
sample = [1, 3, 2, 5, 7, 0, 2, 3]

def mode(values):
    counts = defaultdict(lambda: 0)
    
    for s in values:
        counts[s] += 1
        
    max_count = max(counts.values())
    # List comprehention syntax with filter.
    modes = [v for v in set(values) if counts[v] == max_count]
    return modes

print (mode(sample)) # prints [2, 3].