# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:49:23 2024

@author: chegn
"""

# Solving a system of equations using the approach of
# undoing a matrix build from rhss' of the equations
# by applying an inverse matrix built from the coefficients
# next to unknown variables.

from numpy import array
from numpy.linalg import inv

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

A_matrix = array([ \
    [4, 2, 4], \
    [5, 3, 7], \
    [9, 3, 6]
    ])
    
B_matrix = array([44, 56, 72])

X = inv(A_matrix).dot(B_matrix)

print (X) # x = 2, y = 34, z = -8