# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:47:38 2022

@author: ASUS tayeb
"""

import numpy as np
import pandas as pd
path= r"C:/Users/ASUS/Desktop/sol.xlsx"
data=pd.read_excel(path)
"""print(data)"""
a=0.4934E-2
b=4.0928
c=0.571E-6
d=1.6428
e=0.6763E-3
f=781.334
g=-0.2499
Mw=data.values[:,0]

gravity=data.values[:,1]

T=data.values[:,2]

Ps=data.values[:,3]

RsChunglist=[]
for i in range(T.size):
    RsChung=1/((a*((((141/gravity[i])-131.5)**b)*(((T[i]*(1.8)+32)**c))+(d*((T[i]*(1.8)+32)**e)*np.exp((-f*145.0377*Ps[i])+(g/(145.0377*Ps[i])))))))
    RsChunglist.append(RsChung)
print(RsChunglist)
