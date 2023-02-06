# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file....its actually not now...
"""

import pandas as pd

dft = pd.read_csv('Compiled.csv') 

#Spec Lube
spec = dft.iloc[:,0:2] #gets rid of other lubes

ins = spec[spec['NSt ']== 110].index #indexes trash vaues

spec.drop(ins, inplace = True)
spec.dropna(axis = 0)
spec.reset_index() #removes values

#Wax

wax = dft.iloc[:,2:4] #gets rid of other lubes

inw = wax[wax['Wt']== 110].index #indexes trash vaues

wax.drop(inw, inplace = True)
wax.dropna(axis = 0) #removes values
wax.reset_index()


#Dry

dry = dft.iloc[:,4:6] #gets rid of other lubes

ind = dry[dry['Dt']== 110].index #indexes trash vaues

dry.drop(ind, inplace = True)
dry.dropna(axis = 0) #removes values
dry.reset_index()
#WD40

wd = dft.iloc[:,6:8] #gets rid of other lubes

inwd = wd[wd['WD40t']== 110].index #indexes trash vaues

wd.drop(inwd, inplace = True)
wd.dropna(axis = 0) #removes values
wd.reset_index()
#lithium greez

l = dft.iloc[:,8:10] #gets rid of other lubes

inl = l[l['LGt']== 110].index #indexes trash vaues

l.drop(inl, inplace =  True)
l.dropna(axis = 0) #removes values
l.reset_index()


out = pd.concat([spec,wax,dry,wd,l])

print(out)

out.to_csv('cleaned.csv')