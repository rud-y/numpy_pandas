#%%
import numpy as np
import pandas as pd

my_series = pd.Series([5,10,15,20,25], index=["Day1","Day2","Day3","Day4","Day5",])

print(my_series)
print(my_series.iloc[[1,4]])
print(f"Use iloc index 1: {my_series.iloc[1]}")

print(f".loc Day2-Day3: {my_series.loc["Day1": "Day3"]}")

my_series.index = [0,2,100,3,5]

print(my_series)
print(f"Using .iloc[1:3]: {my_series.iloc[1:3]}")

print(my_series.loc[100:5])
print(f"Using .loc[0:3] : {my_series.loc[0:3]}")

# Index reset
print(f"Resetting index: {my_series.reset_index(drop=True).loc[0:3]}")

# --------- #

# Filtering series , logical test
my_series.loc[my_series.gt("Day3")]
#%%