"""
9. Common NumPy Functions
=============================
Covers: sum(), mean(), max(), min(), argmax(), argmin(),
sort(), unique(), axis=0, axis=1
"""
import numpy as np
arr = np.array([[3, 7, 1],
                 [9, 2, 8],
                 [5, 6, 4]])
print("Array:\n", arr)
# output: Array:
# output:  [[3 7 1]
# output:  [9 2 8]
# output:  [5 6 4]]
print("\nTotal sum:", np.sum(arr))
# output: 
# output: Total sum: 45
print("Sum axis=0 (column-wise):", np.sum(arr, axis=0))
# output: Sum axis=0 (column-wise): [17 15 13]
print("Sum axis=1 (row-wise)   :", np.sum(arr, axis=1))
# output: Sum axis=1 (row-wise)   : [11 19 15]
print("\nMean overall:", np.mean(arr))
# output: 
# output: Mean overall: 5.0
print("Mean axis=0:", np.mean(arr, axis=0))
# output: Mean axis=0: [5.66666667 5.         4.33333333]
print("Mean axis=1:", np.mean(arr, axis=1))
# output: Mean axis=1: [3.66666667 6.33333333 5.        ]
print("\nMax overall:", np.max(arr))
# output: 
# output: Max overall: 9
print("Min overall:", np.min(arr))
# output: Min overall: 1
print("Max axis=0:", np.max(arr, axis=0))
# output: Max axis=0: [9 7 8]
print("Min axis=1:", np.min(arr, axis=1))
# output: Min axis=1: [1 2 4]
print("\nargmax (overall, flattened index):", np.argmax(arr))
# output: 
# output: argmax (overall, flattened index): 3
print("argmin (overall, flattened index):", np.argmin(arr))
# output: argmin (overall, flattened index): 2
print("argmax axis=0:", np.argmax(arr, axis=0))
# output: argmax axis=0: [1 0 1]
print("argmax axis=1:", np.argmax(arr, axis=1))
# output: argmax axis=1: [1 0 1]
print("\nSorted (axis=1, row-wise):\n", np.sort(arr, axis=1))
# output: 
# output: Sorted (axis=1, row-wise):
# output:  [[1 3 7]
# output:  [2 8 9]
# output:  [4 5 6]]
print("Sorted (axis=0, column-wise):\n", np.sort(arr, axis=0))
# output: Sorted (axis=0, column-wise):
# output:  [[3 2 1]
# output:  [5 6 4]
# output:  [9 7 8]]
arr_dup = np.array([1, 2, 2, 3, 3, 3, 4])
print("\nOriginal (with duplicates):", arr_dup)
# output: 
# output: Original (with duplicates): [1 2 2 3 3 3 4]
print("Unique values:", np.unique(arr_dup))
# output: Unique values: [1 2 3 4]
values, counts = np.unique(arr_dup, return_counts=True)
print("Values:", values)
# output: Values: [1 2 3 4]
print("Counts:", counts)
# output: Counts: [1 2 3 1]
