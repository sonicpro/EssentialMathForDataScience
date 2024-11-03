# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 13:41:07 2024

@author: chegn
"""

# Calculating the determinant for a transformation that flips the
# vector space and also scales it.

from numpy.linalg import det
from numpy import array


i_hat = array([-2, 1])
j_hat = array([1, 2])
# Such a basis vectors flip vector space, i.e. the angle between
# i-hat and j-hat is still 90 degree, but j-hat is 90 degree from i-hat
# clockwise.
basis = array([i_hat, j_hat]).transpose()

determinant = det(basis)
# For a transformation that flips space the determinant is negative.
print(determinant)  # prints -5.0