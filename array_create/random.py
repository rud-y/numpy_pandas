#%%
from numpy.random import default_rng

rng = default_rng(12345)

# random_array = rng.random(4)

mean, stddev = 2, 0.2
random_normal = rng.normal(mean, stddev, size=10)
random_normal
# %%
