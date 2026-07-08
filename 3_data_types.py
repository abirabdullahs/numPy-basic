"""
3. Data Types (dtype)
=======================
Covers: Integer, Float, Boolean, String Array, dtype= parameter,
astype(), Type Conversion, Data Type Promotion
"""
import numpy as np
int_arr = np.array([1, 2, 3])
print("Integer Array:", int_arr, "| dtype:", int_arr.dtype)
# output: Integer Array: [1 2 3] | dtype: int64
float_arr = np.array([1.5, 2.5, 3.5])
print("Float Array:", float_arr, "| dtype:", float_arr.dtype)
# output: Float Array: [1.5 2.5 3.5] | dtype: float64
bool_arr = np.array([True, False, True])
print("Boolean Array:", bool_arr, "| dtype:", bool_arr.dtype)
# output: Boolean Array: [ True False  True] | dtype: bool
str_arr = np.array(["apple", "banana", "cherry"])
print("String Array:", str_arr, "| dtype:", str_arr.dtype)
# output: String Array: ['apple' 'banana' 'cherry'] | dtype: <U6
custom_arr = np.array([1, 2, 3], dtype=float)
print("\nCustom dtype (float):", custom_arr, "| dtype:", custom_arr.dtype)
# output: 
# output: Custom dtype (float): [1. 2. 3.] | dtype: float64
custom_arr2 = np.array([1, 2, 3], dtype="int8")
print("Custom dtype (int8):", custom_arr2, "| dtype:", custom_arr2.dtype)
# output: Custom dtype (int8): [1 2 3] | dtype: int8
converted = int_arr.astype(float)
print("\nInt -> Float (astype):", converted, "| dtype:", converted.dtype)
# output: 
# output: Int -> Float (astype): [1. 2. 3.] | dtype: float64
converted2 = float_arr.astype(int)
print("Float -> Int (astype):", converted2, "| dtype:", converted2.dtype)
# output: Float -> Int (astype): [1 2 3] | dtype: int64
mixed_arr = np.array([1, 2, 3.5])
print("\nMixed (int+float) Array:", mixed_arr, "| dtype:", mixed_arr.dtype)
# output: 
# output: Mixed (int+float) Array: [1.  2.  3.5] | dtype: float64
mixed_arr2 = np.array([1, 0, True])
print("Mixed (int+bool) Array:", mixed_arr2, "| dtype:", mixed_arr2.dtype)
# output: Mixed (int+bool) Array: [1 0 1] | dtype: int64
