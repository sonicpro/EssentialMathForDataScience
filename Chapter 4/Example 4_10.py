# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 16:38:05 2024

@author: chegn
"""

# Vector transformation that involves rotation, shear, and 
# flipping the space.
# Basis vectors i-hat and j-hat transform like the following:
# i-hat from [1, 0] to [2, 3]
# j-hat from [0, 1] to [2, -1]
# That way we "flip the space" in sence that j-hat is approx.
# 82 degree clockwise from i-hat rather than 90 degrees counterclockwise.

from numpy import array

# Declare i-hat and j-hat
i_hat = array([2, 3])
j_hat = array([2, -1])

# Compose base matrix using transform, i.e. it looks like
#[[2, 2]
# [3, -1]]

basis = array([i_hat, j_hat]).transpose()

# Declare vector v
v = array([2, 1])

# Create new vector by transforming v with dot product.
# The new vector should be [ (2*2 + 2*1), (3*2 + (-1)*1)] = [6, 5]

new_v = basis.dot(v)

print(new_v) # [6, 5]