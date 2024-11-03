# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:24:28 2024

@author: chegn
"""

# Calculating the determinant for scaling transformation.
from numpy.linalg import det
from numpy import array

i_hat = array([3, 0])
j_hat = array([0, 2])

# Transposed matrix is the same as the non-transposed because
# we swapped 0 with 0.
basis = array([i_hat, j_hat]).transpose()
print("Transposed matrix:\n {}".format(basis))

determinant = det(basis)
print(determinant)  # prints 6.0