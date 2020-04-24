# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:44:16 2020

@author: KarthikMummidisetti
"""

""" 
Random number generation
"""

import numpy as np

print("Random number generation (from Uniform distribution)")
print(np.random.rand(2,3)) # 2 by 3 matrix with random numbers ranging from 0 to 1, Note no Tuple is necessary

print("Numbers from Normal distribution with zero mean and standard deviation 1 i.e. standard normal")
print(np.random.randn(4,3))

print("Random integer vector:",np.random.randint(1,100,10)) #randint (low, high, # of samples to be drawn)
print ("\nRandom integer matrix")
print(np.random.randint(1,100,(4,4))) #randint (low, high, # of samples to be drawn in a tuple to form a matrix)
print("\n20 samples drawn from a dice throw:",np.random.randint(1,7,20)) # 20 samples drawn from a dice throw