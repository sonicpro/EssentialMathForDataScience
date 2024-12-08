# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:52:21 2024

@author: chegn
"""

# Calculating Pearson coefficient using "short" formula from Jamie Dixon's book.
import pandas as pd
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")
Xs = df.values[:, :-1].flatten()
Ys = df.values[:, -1]

from numpy import mean
from math import sqrt
mean_X = mean(Xs)
mean_Y = mean(Ys)
#print('{0},{1}'.format(mean_X, mean_Y))

# Deviation scores:
xs = [ X - mean_X for X in Xs ]
ys = [ Y - mean_Y for Y in Ys ]

#print(dev_scores_X)
#print(dev_scores_Y)

sum_of_devscore_products = sum([ x * y for x, y in zip(xs, ys) ])
sum_of_devscore_X_squared = sum([ x ** 2 for x in xs ])
sum_of_devscore_Y_squared = sum([ y ** 2 for y in ys ])
#print(sum_of_devscore_Y_squared)
#print(sum_of_devscore_products)

# Pearson coefficient:
r = sum_of_devscore_products / sqrt(sum_of_devscore_X_squared * sum_of_devscore_Y_squared)
print(r) #




