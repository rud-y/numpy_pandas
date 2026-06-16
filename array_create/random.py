#%%
from numpy.random import default_rng
import numpy as np

rng = default_rng(12345)

random_array = rng.random(3)
# print(random_array)

mean, stddev = 3, 0.5
random_normal = rng.normal(mean, stddev, size=3)
print(f"random_normal --- {random_normal}")

range = default_rng(12345)
age_range = range.choice(np.arange(30, 45), size=6, replace=False)
print(f"age_range --- {age_range}")

rng2 = np.random.default_rng(5)
random_arr_rng2 = rng2.random(9).reshape(3,3)
print("random range 2 --- ")
# print(random_arr_rng2)

arr_range = np.arange(10,101,10).reshape(5,2)
arr_range
#%%
