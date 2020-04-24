# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:46:49 2020

@author: KarthikMummidisetti
"""

""" 
Reshaping, min, max, sort
"""

import numpy as np
from numpy.random import randint as ri

a = ri(1,100,30)
b = a.reshape(2,3,5)
c = a.reshape(6,5)
print ("Shape of a:", a.shape)
print ("Shape of b:", b.shape)
print ("Shape of c:", c.shape)
print("\na looks like\n",'-'*20,"\n",a,"\n",'-'*20)
print("\nb looks like\n",'-'*20,"\n",b,"\n",'-'*20)
print("\nc looks like\n",'-'*20,"\n",c,"\n",'-'*20)

A = ri(1,100,10) # Vector of random interegrs
print("\nVector of random integers\n",'-'*50,"\n",A)
print("\nHere is the sorted vector\n",'-'*50,"\n",np.sort(A, kind='mergesort'))

M = ri(1,100,25).reshape(5,5) # Matrix of random interegrs
print("\n5x5 Matrix of random integers\n",'-'*50,"\n",M)
print("\nHere is the sorted matrix along each row\n",'-'*50,"\n",np.sort(M, kind='mergesort')) # Default axis =1
print("\nHere is the sorted matrix along each column\n",'-'*50,"\n",np.sort(M, axis=0, kind='mergesort'))


print("Max of a:", a.max())
print("Max of b:", b.max())
print("Max of a location:", a.argmax())
print("Max of b location:", b.argmax())
print("Max of c location:", b.argmax())