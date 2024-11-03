# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:49:38 2024

@author: chegn
"""

# Calculating the determinant for linearly dependend basis vectors.

from numpy.linalg import det
from numpy import array

# Basis vectors are pointing to exactly opposite directions.
i_hat = array([-2, 1])
j_hat = array([3, -1.5])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

print(determinant)  # prints 0