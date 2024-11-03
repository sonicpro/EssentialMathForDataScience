# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:24:32 2024

@author: chegn
"""

# Performing eigendecomposition of a matrix and checking
# the eigenvalue equation Av = lambda v, where v - eigenvector and lambda - eigenvalues.

from numpy import array
from numpy.linalg import eig

A = array([ \
           [1, 2], \
           [4, 5] \
           ])

eigenvals, eigenvecs = eig(A)

print("EIGENVALUES")
print(eigenvals)
print("\nEIGENVECTORS")
print(eigenvecs)

# Trying to grasp the eigenvalue equation.
A_multiplied_by_eigenvector = A @ eigenvecs

# The following is multiplying a vector (eigenvals) to a matrix (eigenvecs).
# The result is a vector, it cannot be the same as the matrix "A_multiplied_by_eigenvector".
eigenvalues_multiplied_by_eigenvector = eigenvals @ eigenvecs

print ("\nA_multiplied_by_eigenvector:\n{}".format(A_multiplied_by_eigenvector))

print("eigenvalues_multiplied_by_eigenvector:\n{}".format( \
                    eigenvalues_multiplied_by_eigenvector))
    
# Conclusion: the eigenvalue equation Av = lambda v means something different than
# multiplication of matrices.
