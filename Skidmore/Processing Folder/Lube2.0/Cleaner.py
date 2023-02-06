# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file....its actually not now...
"""

import pandas as pd

dft = pd.read_csv('Compiled raw.csv') 

#Spec Lube
spec = dft.iloc[:,0:2] #gets rid of other lubes

ins = spec[spec['NSt']== 0].index #indexes trash vaues

spec1 = spec.drop(ins, inplace = False)

spec2 = spec1.dropna(axis = 0)
# print(spec)
spec3 = spec2.reset_index() #removes values
# print(spec)

#Wax

# wax = dft.iloc[:,2:4] #gets rid of other lubes

# inw = wax[wax['Wt']== 0].index #indexes trash vaues

# wax.drop(inw, inplace = True)
# wax.dropna(axis = 0) #removes values
# wax.reset_index()


# #Dry

# dry = dft.iloc[:,6:8] #gets rid of other lubes

# ind = dry[dry['Dt']== 0].index #indexes trash vaues

# dry.drop(ind, inplace = True)
# dry.dropna(axis = 0) #removes values
# dry.reset_index()


# #sptay greez

# l = dft.iloc[:,4:6] #gets rid of other lubes

# inl = l[l['St']== 0].index #indexes trash vaues

# l.drop(inl, inplace =  True)
# l.dropna(axis = 0) #removes values
# l.reset_index()


# out = pd.concat([spec,wax,dry,l])

# print(out)

#out.to_csv('cleaned.csv')