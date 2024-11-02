# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:02:47 2024

@author: chegn
"""

# We have a vector [1, 1]. We need to scale it to become [3, 2].
# We decide to do that using basis matrix vector multiplication (dot product).

from numpy import array

# Declare basis vectors i-hat and j-hat.
i_hat = array([3, 0])
j_hat = array([0, 2])

# In the basis matrix i-hat should represent the first column and j-hat should
# represent the second column. We heed to transpose array of arrays to swap the
# values symmetric to the main diagonal of the matrix.
# Say, i-hat is [3, 5] and j-hat is [7, 2].
# We need the basis matrix is 
#[[3, 7]
# [5, 2]] instead of
#[[3, 5]
# [7, 2]]
basis = array([i_hat, j_hat]).transpose()
# print(basis)

# declare vector v
v = array([1, 1])

# create new vector
# by transforming v with dor product.
new_v = basis.dot(v)

print(new_v) # [3, 2]