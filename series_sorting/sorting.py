#%%
# import numpy as np
import pandas as pd

my_series = pd.Series([5,10,15,20,25], index=["day 1","day 2","day 3","day 4","day 5",])

print(f"{my_series.sort_values(ascending=False)}")

print(f"{}")
#%%