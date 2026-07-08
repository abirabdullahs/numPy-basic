"""
7. Indexing & Slicing
========================
Covers: Positive/Negative Indexing, 2D Indexing,
Slicing (start:stop, :stop, start:, :, step, reverse),
2D Slicing, Row & Column selection
"""
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print("arr[0]:", arr[0])  
# output: arr[0]: 10
print("arr[2]:", arr[2])  
# output: arr[2]: 30
print("\narr[-1]:", arr[-1])  
# output: 
# output: arr[-1]: 50
print("arr[-2]:", arr[-2])    
# output: arr[-2]: 40
arr_2d = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("\n2D Array:\n", arr_2d)
# output: 
# output: 2D Array:
# output:  [[1 2 3]
# output:  [4 5 6]
# output:  [7 8 9]]
print("arr_2d[0,0]:", arr_2d[0, 0])  
# output: arr_2d[0,0]: 1
print("arr_2d[1,2]:", arr_2d[1, 2])  
# output: arr_2d[1,2]: 6
print("arr_2d[-1,-1]:", arr_2d[-1, -1]) 
# output: arr_2d[-1,-1]: 9
print("\narr[1:4]  (start:stop):", arr[1:4])
# output: 
# output: arr[1:4]  (start:stop): [20 30 40]
print("arr[:3]   (:stop)      :", arr[:3])
# output: arr[:3]   (:stop)      : [10 20 30]
print("arr[2:]   (start:)     :", arr[2:])
# output: arr[2:]   (start:)     : [30 40 50]
print("arr[:]    (all)        :", arr[:])
# output: arr[:]    (all)        : [10 20 30 40 50]
print("arr[::2]  (step)       :", arr[::2])
# output: arr[::2]  (step)       : [10 30 50]
print("arr[::-1] (reverse)    :", arr[::-1])
# output: arr[::-1] (reverse)    : [50 40 30 20 10]
print("\n2D Slicing arr_2d[0:2, 0:2]:\n", arr_2d[0:2, 0:2])
# output: 
# output: 2D Slicing arr_2d[0:2, 0:2]:
# output:  [[1 2]
# output:  [4 5]]
print("\nRow 0:", arr_2d[0])      
# output: 
# output: Row 0: [1 2 3]
print("Row 1:", arr_2d[1, :])     
# output: Row 1: [4 5 6]
print("\nColumn 0:", arr_2d[:, 0])  
# output: 
# output: Column 0: [1 4 7]
print("Column 2:", arr_2d[:, 2])    
# output: Column 2: [3 6 9]
