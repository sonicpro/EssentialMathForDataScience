# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:19:21 2024

@author: chegn
"""
# Getting an inverse matrix using sympy
from sympy import *

# 4x + 2y + 4z = 44
# 5x + 3y + 7z = 56
# 9x + 3y + 6z = 72

first_equation_coeffs = [4, 2, 4]
second_equation_coeffs = [5, 3, 7]
third_equation_coeffs = [9, 3, 6]

A_matrix = Matrix([ \
                  first_equation_coeffs, \
                  second_equation_coeffs, \
                  third_equation_coeffs \
                  ])
    
A_inverse_matrix = A_matrix.inv()
print("INVERSE: {}".format(A_inverse_matrix))
identity_matrix = A_inverse_matrix @ A_matrix
print("IDENTITY: {}".format(identity_matrix))

