# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:06:40 2024

@author: chegn
"""

# Calculate the sum of squared residuals based on the data from Example 5_1
# and the linear regression we calculated for that data in Example 5_1.

# Import points though pandas
import pandas as pd
points = pd.read_csv('https://bit.ly/3goOAnt', delimiter = ",").itertuples()

# The slope and the intercept were calculated in Example 5_1.
slope = 1.93939
intercept = 4.73333

sum_of_squares = 0.0

# Calculate the residuals
for p in points:
    y_actual = p.y
    y_predict = slope * p.x + intercept
    squared_residual = (y_actual - y_predict)**2
    sum_of_squares += squared_residual
    
print("sum of squares = {}".format(sum_of_squares))
# sum of squares = 28.096969704500005