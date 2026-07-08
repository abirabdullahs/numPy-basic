"""
5. Random Array Generation
=============================
Covers: np.random.rand(), np.random.randint(), np.random.randn(),
np.random.choice(), np.random.seed()
"""
import numpy as np
np.random.seed(42) 
rand_arr = np.random.rand(3)         
print("np.random.rand(3):", rand_arr)
# output: np.random.rand(3): [0.37454012 0.95071431 0.73199394]
rand_2d = np.random.rand(2, 3)       
print("\nnp.random.rand(2,3):\n", rand_2d)
# output: 
# output: np.random.rand(2,3):
# output:  [[0.59865848 0.15601864 0.15599452]
# output:  [0.05808361 0.86617615 0.60111501]]
randint_arr = np.random.randint(1, 10, size=5)  
print("\nnp.random.randint(1,10,5):", randint_arr)
# output: 
# output: np.random.randint(1,10,5): [8 3 6 5 2]
randint_2d = np.random.randint(0, 100, size=(2, 3))
print("np.random.randint 2D:\n", randint_2d)
# output: np.random.randint 2D:
# output:  [[87 29 37]
# output:  [ 1 63 59]]
randn_arr = np.random.randn(5)
print("\nnp.random.randn(5):", randn_arr)
# output: 
# output: np.random.randn(5): [-0.57138017 -0.92408284 -2.61254901  0.95036968  0.81644508]
choice_arr = np.random.choice([10, 20, 30, 40, 50], size=3)
print("\nnp.random.choice:", choice_arr)
# output: 
# output: np.random.choice: [20 40 40]
choice_no_repeat = np.random.choice([1, 2, 3, 4, 5], size=3, replace=False)
print("np.random.choice (no repeat):", choice_no_repeat)
# output: np.random.choice (no repeat): [1 2 5]
