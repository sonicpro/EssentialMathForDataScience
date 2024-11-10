# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:59:34 2024

@author: chegn
"""

# Using QR matrix decomposition from linalg to do simple
# linear regression.

import pandas as pd
from numpy.linalg import qr, inv
import numpy as np

# Import points
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Extract input variables (all rows, all columns but last column).
X = df.values[:, :-1].flatten()

# We should convert the vector X to a matrix with the second column
# containing all "1".
X_1 = np.vstack([X, np.ones(len(X))]) # This will rotate X horizontally
# adding the second row of "1". X.shape was (10,). X_1 shape is (2, 10).
# print(X.shape)
# print(X_1.shape)
# We also must transpose X_1 so that the X is the first column, "1"s are
# the second column.
X_1 = X_1.transpose()

# Extract output column (all rows, last column).
Y = df.values[:, -1]

# Calculate "beta" coefficients for slope and intercept.
# They are returned as array, beta0 (intercept) on index 0 and
# beta1 (slope) on index 1.
Q, R = qr(X_1)
# print(Q.shape)
b = (inv(R) @ Q.transpose()).dot(Y)
# print(Y.shape)
print(b) # [1.93939394, 4,73333333]