#%%
import numpy as np
from numpy.random import default_rng

integer_arr = np.arange(12)
print(f"array position -2: {integer_arr[-2]}")

# Slice
print(integer_arr[:3])
print(integer_arr[::3])
# [0, 3, 6, 9]

new_array = integer_arr.reshape(3,4)
print(f"new_array reshape(3,4) ---- {new_array}")
print(f"What??  ---{new_array[:, 1:]}")

ages = np.array([5, 10, 15, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])

youth_ages = ages[1:4]

print(f"youth ages ---- {youth_ages}")

# Accessing rows and columns or specific elements of an array
rng = default_rng(12345)
random_array = rng.random(9)

array3matrix = random_array.reshape(3, 3)

print(f"array3matrix ----- {array3matrix}")

# Access only last row
print(f"Last row --- {array3matrix[2, :]}")

# Access middle column
print(f"Middle column --- {array3matrix[:, 1]}")

# Access only first element of the last column
print(f"First element of the last column --- {array3matrix[0, 2]}")

# %%
