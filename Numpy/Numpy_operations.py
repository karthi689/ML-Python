# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:38:34 2020

@author: KarthikMummidisetti

NumPy Operations
"""

""" 
Vectors and matrices
"""

my_list = [1,2,3]
import numpy as np
arr = np.array(my_list)
print("Type/Class of this object: ", type(arr))
print("Here is the vector\n--------------------\n", arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)
print("Type/Class of this object: ", type(mat))
print("Here is the matrix\n----------\n", mat,"\n----------")
print("Dimension of this matrix: ", mat.ndim, sep = '') #ndim gives the dimensison, 2 for a matrix, 1 for a vector
print("Size of this matrix: ", mat.size, sep = '') #size gives the total number of elements
print("Shape of this matrix: ", mat.shape, sep = '') #shape gives the number of elements along each axes (dimension)
print("Data type of this matrix: ", mat.dtype, sep = '') #dtype gives the data type contained in the array

my_mat = [[1.1,2,3],[4,5.2,6],[7,8.3,9]]
mat = np.array(my_mat)
print("Data type of the modified matrix: ", mat.dtype, sep = '') #dtype gives the data type contained in the array
print("\n\nEven tuples can be converted to ndarrays...")

my_mat_tup = np.array([(1.5,2,3), (4,5,6)])
print("We write b = np.array([(1.5,2,3), (4,5,6)])")
print("Matrix made from tuples, not lists\n---------------------------------------")
print(my_mat_tup)


""" 
arange and linspace
"""

print("A series of numbers:",np.arange(5,16)) # A series of numbers from low to high
print("Numbers spaced apart by 2:",np.arange(0,11,2)) # Numbers spaced apart by 2
print("Numbers spaced apart by float:",np.arange(0,11,2.5)) # Numbers spaced apart by 2.5
print("Every 5th number from 50 in reverse order\n",np.arange(50,-1,-5))

print("21 linearly spaced numbers between 1 and 5\n--------------------------------------------")
print(np.linspace(1,5,21))
