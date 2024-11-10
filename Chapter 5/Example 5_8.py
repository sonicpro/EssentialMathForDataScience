# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:18:39 2024

@author: chegn
"""

# "Gradient descent" technique demo.
# Let's find the lowest point of the parabola curve of f(x) = (x - 3)^2 + 4
# function.

import random

def f(x):
    return (x - 3) ** 2 + 4

# The derivative d/dx_f(x) is 2 * (x - 3)
def dx_f(x):
    return 2 * (x - 3)

# The learning rate
L = 0.001

# The number of iterations to perform gradient descent.
iterations = 100_000 # 10_000 is already provides a decent result of x = 2.9999999818174246

# Start gradient descent at a random x.
x = random.randint(-15, 15)

# Python way to loop 100_000 times.
for i in range(iterations) :
    # Get slope. If, say the initial x was 15, d/dx_f(x) = (15 - 3)^2 = 144.
    # It is how much the tangent line at x = 15 increases on y axis
    # for an increase on x axis of 1.
    d_x = dx_f(x)
    # Despite d_x (slope) is how fast f(x) changes for the defined x change
    # we do subtract it from x rather than from y = f(x).
    # We subtract a part of "learning rate" proportional to the amount of
    # slope at a last computed x point. With more iterations the
    # slope becomes closer to 0 and x is approximate the lowest point
    # of the function.
    x -= L * d_x
    
print(x, f(x)) # prints 2.999999999999889 4.0

