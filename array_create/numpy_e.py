#%%
import numpy as np

arr_2d = np.array([range(1,11), range(1,11), range(1,11)])

# print(f"{arr_2d.shape}")
# print(f"{arr_2d.size}")
print(f"{arr_2d.T.shape}")
# print(f"{arr_2d.dtype}")

np.array(["Time","to","learn"])

arr1 = np.array(range(10, 100, 10))
# print(f"{arr1}")
# print(f"{arr1.reshape(3,3)}")

arr_create1 = np.linspace(0, 1, 6), 
print(f"{arr_create1}")

arr_create2 = np.ones(3,)
# print(f"{arr_create2}")

arr_create3 = np.arange(1,17,2).reshape(4,2)
print(f"{arr_create3}")

# np.zeros((5, 10), 'int')
# np.identity(4)

np.arange(10).reshape(5, 2)

print('------------')
my_array = np.array([10, 32, 13, 14, 51, 6])
average_val = my_array.mean()
print("Avg value: ", average_val)
# %%

