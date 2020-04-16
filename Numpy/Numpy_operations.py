# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:38:34 2020

@author: KarthikMummidisetti
"""

""" 
NumPy Operations

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