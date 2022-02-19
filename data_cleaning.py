# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:21:36 2022

@author: kira
"""

import pandas as pd
import os
os.chdir('C:\\Users\\Frank Wan\\Desktop\\Projects')
data = pd.read_csv('query_20211221_082058.csv', sep='delimiter')
data
columns = data.columns.str.split('|',expand=True)
name = list(columns[0])

df = data. iloc[:, 0].str.split('|',expand=True)
N = 3
# Drop last N columns of dataframe
for i in range(N):
        del df[df.columns.values[-1]]
df
df.columns = name
df
