# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:19:21 2024

@author: chegn
"""

from numpy import array

first_equation_coeffs = [4, 2, 4]
second_equation_coeffs = [5, 3, 7]
third_equation_coeffs = [9, 3, 6]

A_matrix = array([ \
                  first_equation_coeffs, \
                  second_equation_coeffs, \
                  third_equation_coeffs \
                  ])
    
first_row_of_A_inverse_matrix = array([ -1.0 / 2.0, 0, 1.0 / 3.0 ])
second_row_of_A_inverse_matrix = array([ 5.5, -2, -4.0 / 3.0 ])
third_row_of_A_inverse_matrix = array([ -2, 1, 1.0 / 3.0 ])

A_inverse_matrix = array([ \
                          first_row_of_A_inverse_matrix, \
                          second_row_of_A_inverse_matrix, \
                          third_row_of_A_inverse_matrix \
                        ])

identity_matrix = A_inverse_matrix @ A_matrix
print(identity_matrix)

try_to_get_identity_matrix_from_reverse_multiplication = \
    A_matrix @ A_inverse_matrix
    
print(try_to_get_identity_matrix_from_reverse_multiplication)

# The results are the same, the inverse matrices multiplication
# is commutative.