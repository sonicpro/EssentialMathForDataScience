# -*- coding: utf-8 -*-

# Assestment 4_5. Solving system of equations using linear transformations.
# The approach in algebraic notion is Ax = B, where A - transformation matrix,
# B - resulting vector, and x - the vector built from unknown variables.

# We can draw similarity with finding unknown multiplier in a * x = b equation.
# Here we "undo" b by multiplying both sides on (1 / a).

# In case of matrices, we multiply both sides on a matrix inverse to A denoted as
# A-1. The same as with numbers, where a * (1 / a) equals 1, the product of
# A * A-1 produces identity matrix, a.k.a matrix that returns the same vector
# being multiplied on any vector.
# A-1 A x = A-1 B
# (A-1 A) x = A-1 B, and (A-1 A) produce the identity matrix
# x = A-1 B.

from numpy.linalg import inv
from numpy import array

# 3x + 1y + 0z = 54
# 2x + 4y + 1z = 12
# 3x + 1y + 8z = 6
A = array([ \
           [3, 1, 0], \
           [2, 4, 1], \
           [3, 1, 8] \
        ])
    
B = array([54, 12, 6])

x = inv(A).dot(B)
print ("The unknown variables x, y, z are {}".format(x))