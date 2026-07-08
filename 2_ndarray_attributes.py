"""
2. ndarray and Its Attributes
==============================
Covers: shape, ndim, size, dtype, itemsize, nbytes
"""
import numpy as np
arr = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("Array:\n", arr)
# output: Array:
# output:  [[1 2 3]
# output:  [4 5 6]]
print("\nshape   :", arr.shape)    
# output: 
# output: shape   : (2, 3)
print("ndim    :", arr.ndim)       
# output: ndim    : 2
print("size    :", arr.size)       
# output: size    : 6
print("dtype   :", arr.dtype)      
# output: dtype   : int64
print("itemsize:", arr.itemsize, "bytes") 
# output: itemsize: 8 bytes
print("nbytes  :", arr.nbytes, "bytes")   
# output: nbytes  : 48 bytes
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array shape:", arr_3d.shape)
# output: 
# output: 3D Array shape: (2, 2, 2)
print("3D Array ndim :", arr_3d.ndim)
# output: 3D Array ndim : 3
print("3D Array size :", arr_3d.size)
# output: 3D Array size : 8
