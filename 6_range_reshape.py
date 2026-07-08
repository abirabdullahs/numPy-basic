"""
6. Creating Arrays from Range
================================
Covers: np.arange(), np.linspace(), reshape(), reshape(-1)
"""
import numpy as np
arr1 = np.arange(10)             
print("np.arange(10):", arr1)
# output: np.arange(10): [0 1 2 3 4 5 6 7 8 9]
arr2 = np.arange(2, 20, 2)       
print("np.arange(2,20,2):", arr2)
# output: np.arange(2,20,2): [ 2  4  6  8 10 12 14 16 18]
arr3 = np.linspace(0, 1, 5)      
print("\nnp.linspace(0,1,5):", arr3)
# output: 
# output: np.linspace(0,1,5): [0.   0.25 0.5  0.75 1.  ]
arr4 = np.linspace(0, 100, 6)
print("np.linspace(0,100,6):", arr4)
# output: np.linspace(0,100,6): [  0.  20.  40.  60.  80. 100.]
arr5 = np.arange(12)
print("\nOriginal 1D array:", arr5)
# output: 
# output: Original 1D array: [ 0  1  2  3  4  5  6  7  8  9 10 11]
reshaped = arr5.reshape(3, 4)    
print("Reshaped (3,4):\n", reshaped)
# output: Reshaped (3,4):
# output:  [[ 0  1  2  3]
# output:  [ 4  5  6  7]
# output:  [ 8  9 10 11]]
reshaped2 = arr5.reshape(2, 2, 3)
print("Reshaped (2,2,3):\n", reshaped2)
# output: Reshaped (2,2,3):
# output:  [[[ 0  1  2]
# output:   [ 3  4  5]]
# output: 
# output:  [[ 6  7  8]
# output:   [ 9 10 11]]]
flat_again = reshaped.reshape(-1)    
print("\nreshape(-1) -> flatten:", flat_again)
# output: 
# output: reshape(-1) -> flatten: [ 0  1  2  3  4  5  6  7  8  9 10 11]
auto_reshape = arr5.reshape(4, -1)   
print("reshape(4,-1):\n", auto_reshape)
# output: reshape(4,-1):
# output:  [[ 0  1  2]
# output:  [ 3  4  5]
# output:  [ 6  7  8]
# output:  [ 9 10 11]]
