# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:12:08 2019

@author: zacd
"""

import pandas as pd
import numpy as np
from scipy import stats

dft = pd.read_csv('knorm_forpython.csv')

a = pd.DataFrame(dft)

b = a.iloc[:,0:1].dropna()
c = a.iloc[:,1:2].dropna()

b.to_numpy

c.to_numpy

d = np.swapaxes(b,0,1)

e = np.swapaxes(c,0,1)

print(d)
print(e)

slope, intercept, r_value, p_value, std_err = stats.linregress(e,d)
print("slope: %f   intercept: %f p_value: %f"   % (slope, intercept,p_value))





