# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:18:41 2024

@author: chegn
"""

# v landed at [1 2]. Being transformation with i-hat of [-2 1] and j-hat of
# [1 -2] applied to v, where does it land?

from numpy import array

i_hat = array([-2, 1])
j_hat = array([1, -2])
transform = array([i_hat, j_hat]).transpose()

v = array([1, 2])

new_v = transform.dot(v)

print ("The transformed vector lands at {}".format(new_v))