# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:20:06 2024

@author: chegn
"""

# Example 1.25. "Chain rule" for derivative of a function when
# we can decouple the function to two linked functions.
# The first of the linked functions is y = x**2 + 1. The second
# of the linked functions is z = y**3 - 2. We need to find a
# derivative dz / dx.

from sympy import symbols, diff

x, y = symbols('x y')

# dy / dx.
_y = x**2 + 1
dy_dx = diff(_y)

# dz / dy
z = y**3 - 2
dz_dy = diff(z)

# Calculate dz / dx without chain rule.
# Step 1 - get rid of y in the second function:
z_of_x = z.subs(y, _y)
# Step 2 - get the derivative.
dz_dx_no_chain = diff(z_of_x)

# Calculate dz / dx with chain rule.
# Step 1 - multiply the derivatives of the first and the second
# functions.
dz_dx_of_x_and_y = dy_dx * dz_dy
# Step 2 - get rid of y.
dz_dx_chain = dz_dx_of_x_and_y.subs(y, _y)

# Prove chain rule to show that both are equal.
print(dz_dx_no_chain) # 6*x*(x**2 + 1)**2
print(dz_dx_chain)    # 6*x*(x**2 + 1)**2