# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:15:00 2024

@author: chegn
"""

# Exploring the central limit theorem.
# Proving that avarages of the samples taken of a large striclty uniform
# population avarage out in a normal distribution. I.e. if we plot the bars of
# equal width and the height of each bar is proportional to a number of avarages
# that are in x1, x2 range of the bar limits, the bars form a bell-curved histogram.

import random
import plotly.express as px
import plotly.io as pio
pio.renderers.default="svg"

# The population should be "big". Ours is at least of
# 31 * 1000 = 31000 data points.

sample_size = 31
sample_count = 1000

# Calculating 31 averages:
x_values = [ \
    (sum([ random.uniform(0.0, 1.0) for i in range(sample_size) ]) \
      / sample_size) \
        for _ in range(sample_count) \
    ]

# Each bar will be of width 1.
y_values = [ 1 for _ in range(sample_count) ]

# Validating the property 3 of sample limit theorem: if the population is not 
# normal (ours is uniform), but the sample size is greater than 30 (ours is 31),
# the sample means form roughly normal distribution.
fig = px.histogram(x=x_values, y=y_values, nbins=20)
fig.show()

# Validating the properties 1 of the sample limit theorem.
# Property 1. The population mean is equal to the mean of sample means.
uniform_population_of_size_31K = [ random.uniform(0.0, 1.0) for i in range(31000) ]
population_mean = sum(uniform_population_of_size_31K) / 31000
# calculating sample means. [::31] means "slice bracket with start undefined,
# end undefined and step size of 31.
samples = [ list(uniform_population_of_size_31K[i:i+31]) for i in \
    range(31000)[::31] ]
x_values2 = [ sum(i) / 31 for i in samples ]
mean_of_sample_means = sum(x_values2) / 1000
print("Population mean: {}".format(population_mean)) # prints 0.5014818860114387
print("Mean of sample means: {}".format(mean_of_sample_means)) # prints 0.5014818860114387