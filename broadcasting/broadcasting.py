#%%
import numpy as np

test_arr = np.array([[1,2,3], [1,2,3], [1,2,3]])

print(f"array broadcast + 1: {test_arr + np.array([1,10,20])}")
print(f"array broadcast and reshape: {test_arr + np.array([5,5,5])}")

# !!!
print(f"array broadcast and reshape !!! : {test_arr[0, :] + test_arr[:, 1].reshape(3, 1)}")



#%%