# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:34:47 2024

@author: chegn
"""

# Calculating determinant for shear transformation

from numpy.linalg import det
from numpy import array

i_hat = array([1, 0])
j_hat = array([1, 1])

basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)

# A shear without a scale does not change the determinant.
# The area of the vector space of the basis matrix is the same than
# for the identity matrix [[1 0]
#                          [0 1]]
print (determinant)  # prints 1.0