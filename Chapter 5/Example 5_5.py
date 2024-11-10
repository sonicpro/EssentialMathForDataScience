# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:24:44 2024

@author: chegn
"""

# Calculating the slope and the intercept for a simple
# linear regression using closed form equation.

import pandas as pd

# Load the data
points = list(pd.read_csv('https://bit.ly/3goOAnt', delimiter=",").itertuples())

n = len(points)

slope = (n*sum(p.x*p.y for p in points) - sum(p.x for p in points) * sum(p.y for p in points)) / \
    (n*sum(p.x**2 for p in points) - sum(p.x for p in points)**2)
    
intercept = sum(p.y for p in points) / n - slope * sum(p.x for p in points) / n

print (slope, intercept)
# 1.9393939393939394 4.7333333333333325