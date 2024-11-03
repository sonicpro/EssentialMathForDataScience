# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:15:38 2024

@author: chegn
"""

# Combining two transformations.

from numpy import array
# Transformation 1 - rotation. Basis matrix is
#[[0 -1]
# [1 0]].
i_hat1 = array([0, 1])
j_hat1 = array([-1, 0])
transform1 = array([i_hat1, j_hat1]).transpose()

# Transformation 2 - shear. Basis matrix is
#[[1 1]
# [0 1]]
i_hat2 = array([1, 0])
j_hat2 = array([1, 1])
transform2 = array([i_hat2, j_hat2]).transpose()

# Combine Transformations. @ is an alias for matmul(). matmul() does
# the same as dot() but is is optimized for matrix operations.
# Matrixes should be multiplied outermost transformation lhs and
# the innermost transformation rhs.
combined = transform2 @ transform1

# Test. Should be
# [[1 -1]
#  [1 0]]
print("COMBINED MATRIX:\n {}".format(combined))

v = array([1, 2])
print(combined.dot(v))  # [-1 1]