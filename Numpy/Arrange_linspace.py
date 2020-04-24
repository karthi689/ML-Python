# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:43:00 2020

@author: KarthikMummidisetti
"""

""" 
arange and linspace
"""

import numpy as np

print("A series of numbers:",np.arange(5,16)) # A series of numbers from low to high
print("Numbers spaced apart by 2:",np.arange(0,11,2)) # Numbers spaced apart by 2
print("Numbers spaced apart by float:",np.arange(0,11,2.5)) # Numbers spaced apart by 2.5
print("Every 5th number from 50 in reverse order\n",np.arange(50,-1,-5))

print("21 linearly spaced numbers between 1 and 5\n--------------------------------------------")
print(np.linspace(1,5,21))