#%%
from numpy.random import default_rng
import numpy as np

rng = default_rng(12345)

random_array = rng.random(3)
# print(random_array)

mean, stddev = 1, 0.5
random_normal = rng.normal(mean, stddev, size=3)
print(f"rantom_normal>> {random_normal}")

rng = default_rng(12345)
age_range = rng.integers(1,101,10)
print(age_range)

rng2 = np.random.default_rng(2022)
random_arr_rng2 = rng2.random(9).reshape(3,3)
print(random_arr_rng2)

arr_range = np.arange(10,101,10).reshape(5,2)
arr_range
#%%
