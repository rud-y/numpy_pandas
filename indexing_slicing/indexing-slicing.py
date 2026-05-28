#%%
import numpy as np

integer_arr = np.arange(12)
print(f"array position -2: {integer_arr[-2]}")

# Slice
print(integer_arr[:3])
print(integer_arr[::3])
# [0, 3, 6, 9]

new_array = integer_arr.reshape(3,4)
# print(new_array)
print(new_array[:, 1:])

ages = np.array([5, 10, 15, 19, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
ages[::3]

# youth_ages = ages[10]
# %%
