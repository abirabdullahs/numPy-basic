"""
8. Copy, View & Advanced Indexing
=====================================
Covers: copy(), view(), Boolean Indexing, Fancy Indexing,
Iteration (Loop), Nested Loop
"""
import numpy as np
original = np.array([1, 2, 3, 4, 5])
copied = original.copy()
copied[0] = 100
print("Original:", original)  
# output: Original: [1 2 3 4 5]
print("Copied  :", copied)
# output: Copied  : [100   2   3   4   5]
viewed = original.view()
viewed[0] = 999
print("\nOriginal after view change:", original) 
# output: 
# output: Original after view change: [999   2   3   4   5]
print("Viewed:", viewed)
# output: Viewed: [999   2   3   4   5]
arr = np.array([10, 15, 20, 25, 30, 35])
print("\nArray:", arr)
# output: 
# output: Array: [10 15 20 25 30 35]
print("Elements > 20:", arr[arr > 20])
# output: Elements > 20: [25 30 35]
print("Even elements:", arr[arr % 2 == 0])
# output: Even elements: [10 20 30]
condition = (arr > 10) & (arr < 30)
print("10 < x < 30:", arr[condition])
# output: 10 < x < 30: [15 20 25]
print("\nFancy Indexing arr[[0,2,4]]:", arr[[0, 2, 4]])
# output: 
# output: Fancy Indexing arr[[0,2,4]]: [10 20 30]
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Fancy Indexing 2D arr_2d[[0,2]]:\n", arr_2d[[0, 2]])
# output: Fancy Indexing 2D arr_2d[[0,2]]:
# output:  [[1 2 3]
# output:  [7 8 9]]
print("\n1D Array Iteration:")
# output: 
# output: 1D Array Iteration:
for x in arr:
    print(x, end=" ")
# output: 10 15 20 25 30 35 
print()
print("\n2D Array Nested Loop:")
# output: 
# output: 2D Array Nested Loop:
for row in arr_2d:
    for val in row:
        print(val, end=" ")
    print() 
# output: 1 2 3 
# output: 4 5 6 
# output: 7 8 9 
print("\nUsing np.nditer():")
# output: 
# output: Using np.nditer():
for val in np.nditer(arr_2d):
    print(val, end=" ")
# output: 1 2 3 4 5 6 7 8 9 
print()
