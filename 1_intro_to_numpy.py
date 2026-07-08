"""
1. Introduction to NumPy
=========================
Covers: NumPy কী, কেন ব্যবহার, import, array তৈরি, 1D/2D/3D array, List vs NumPy Array
"""
import numpy as np
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])
print("Python List:", python_list)
# output: Python List: [1, 2, 3, 4, 5]
print("NumPy Array:", numpy_array)
# output: NumPy Array: [1 2 3 4 5]
try:
    print(python_list * 2) 
except Exception as e:
    print("Error:", e)
# output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("NumPy Array * 2 =", numpy_array * 2) 
# output: NumPy Array * 2 = [ 2  4  6  8 10]
arr_1d = np.array([10, 20, 30, 40])
print("\n1D Array:", arr_1d)
# output: 
# output: 1D Array: [10 20 30 40]
arr_2d = np.array([[1, 2, 3],
                    [4, 5, 6]])
print("\n2D Array:\n", arr_2d)
# output: 
# output: 2D Array:
# output:  [[1 2 3]
# output:  [4 5 6]]
arr_3d = np.array([[[1, 2], [3, 4]],
                    [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr_3d)
# output: 
# output: 3D Array:
# output:  [[[1 2]
# output:   [3 4]]
# output: 
# output:  [[5 6]
# output:   [7 8]]]
