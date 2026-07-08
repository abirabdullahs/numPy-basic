"""
4. Creating Arrays
====================
Covers: List থেকে Array, Tuple থেকে Array, Nested List -> 2D,
Nested Nested List -> 3D, Existing Array থেকে নতুন Array
"""
import numpy as np
list_arr = np.array([1, 2, 3, 4])
print("List থেকে Array:", list_arr)
# output: List থেকে Array: [1 2 3 4]
tuple_arr = np.array((10, 20, 30))
print("Tuple থেকে Array:", tuple_arr)
# output: Tuple থেকে Array: [10 20 30]
nested_list = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(nested_list)
print("\nNested List -> 2D Array:\n", arr_2d)
# output: 
# output: Nested List -> 2D Array:
# output:  [[1 2 3]
# output:  [4 5 6]]
nested_nested = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
arr_3d = np.array(nested_nested)
print("\nNested Nested List -> 3D Array:\n", arr_3d)
# output: 
# output: Nested Nested List -> 3D Array:
# output:  [[[1 2]
# output:   [3 4]]
# output: 
# output:  [[5 6]
# output:   [7 8]]]
original = np.array([1, 2, 3, 4, 5])
new_from_existing = np.array(original)     
print("\nOriginal Array:", original)
# output: 
# output: Original Array: [1 2 3 4 5]
print("New Array (from existing):", new_from_existing)
# output: New Array (from existing): [1 2 3 4 5]
new_from_existing[0] = 100
print("Modified New Array:", new_from_existing)
# output: Modified New Array: [100   2   3   4   5]
print("Original (unchanged):", original)
# output: Original (unchanged): [1 2 3 4 5]
