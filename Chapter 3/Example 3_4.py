# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:44:40 2024

@author: chegn
"""

# Example 3_4 calculatin the median.
# Number of pets each person owns.
sample = [1, 3, 2, 5, 7, 0, 2, 3]

def median(values):
    ordered = sorted(values)
    print(ordered)
    n = len(ordered)
    mid = int(n / 2) - 1 if n % 2 == 0 else int(n / 2)
    
    if n % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2.0
    else:
        return ordered[mid]
    
print(median(sample)) #prints 2.5.
