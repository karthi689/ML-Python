# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:45:18 2020

@author: KarthikMummidisetti
"""

""" 
Zeroes, Ones, empty, and Identity matrix
"""

import numpy as np

print("Vector of zeroes\n---------------------")
print(np.zeros(5))
print("Matrix of zeroes\n--------------------")
print(np.zeros((3,4))) # Notice Tuples

print("Vector of ones\n---------------------")
print(np.ones(5))
print("Matrix of ones\n---------------------")
print(np.ones((5,2))) # Note matrix dimension specified by Tuples
print("Matrix of 5's\n---------------------")
print(5*np.ones((3,5)))

print("Empty matrix\n-------------\n", np.empty((3,5)))

mat1 = np.eye(4) 
print("Identity matrix of dimension", mat1.shape)
print(mat1)