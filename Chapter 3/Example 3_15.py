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

# The population should be "big" ours is at least of
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

# plotly has a special "histogram" function for plotting
# the number of points in the "bins".
fig = px.histogram(x=x_values, y=y_values, nbins=20)
fig.show()