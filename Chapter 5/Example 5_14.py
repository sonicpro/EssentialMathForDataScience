# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:07:45 2024

@author: chegn
"""

# Calculating correlation coefficient using Pandas.
import pandas as pd

# Read data into pandas dataframe.
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# Getting Pearson's coefficient from the dataframe.
# Dataframe returns 2 x 2 matrix for correlations - x of y,  x of x, y of y, y of x.
correlations = df.corr(method='pearson')

print(correlations)