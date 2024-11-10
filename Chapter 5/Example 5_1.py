# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:15:15 2024

@author: chegn
"""

# On guthubusercontent there is a csv data that contains
# number of vet visits of a dog of certain age.

# We are going to do linear regression of that data using scikit-learn.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Import data through pandas.
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Extract input variables (all rows, all colums but last column)
X = df.values[:, :-1]

# Extract output variables (all rows, last column)
Y = df.values[:, -1]

# Fit a line to the points
fit = LinearRegression().fit(X, Y)

# Calcularing the slope and the intercept.
slope = fit.coef_[0] # coef_ is numpy.ndarray, take the first value.
intercept = fit.intercept_
print("slope = {}".format(slope))
print("intercept = {}".format(intercept))

# Show in chart
plt.plot(X, Y, 'o') # scatterplot
plt.plot(X, slope * X + intercept) # line
plt.show