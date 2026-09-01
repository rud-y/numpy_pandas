#%%
import numpy as np
import pandas as pd

# Create dataFrame from oil.csv ( drop missing values)
oil = pd.read_csv("../csv/oil.csv").dropna()

oil_array = np.array(oil["dcoilwtico"].iloc[800:900])

oil_series = pd.Series(oil_array, name="Oil Prices")
print(f"Oil series 100 items: {oil_series}")

# Dates
dates = np.array(oil["date"].iloc[800:900])
oil_series.index = dates


print(f"Oil mean: {oil_series.mean()}")

int_oil_series = oil_series.astype("int64")
# print(f"Int Oil mean: {int_oil_series.mean()}")
# print(f"{int_oil_series[2]}")
# print(f"dtype int_oil_series: {int_oil_series.dtype}")


# .iloc(), .loc()
print(f"First three - mean: {oil_series[:3].mean().round(2)}")
print(f"Last ten - mean: {oil_series[-10:].mean()}")

print("Oil prices from January 1 2017 - January 11 2017:")
# print(oil_series.loc['2017-01-01' : '2017-01-11'])
# print(oil_series.loc['2017-01-01' : '2017-01-11'].size)
print(oil_series.loc['2017-01-01' : '2017-01-11'].reset_index(drop=True))

print(f"gt() : {oil_series.gt(52)}")


my_series = pd.Series([5,10,15,20,25], index=["day 1","day 2","day 3","day 4","day 5",])

# print(f"my_series -- {my_series == 2}")
print(f">>>Values excluding 10 and 25: {my_series.loc[~my_series.isin([10, 25])]}")

print(f">>>Greater than 15: {my_series.loc[my_series.gt(15)]}")

print(f"Is 15 present: {my_series.isin([15])}")

mask = ((my_series.le(20)) & (my_series > 5))
print(f">>>More than 5 & including 20: {my_series.loc[mask]}")

my_series = my_series.reset_index(drop=True)
print(f"Reset index my_series: \n{my_series}")


# Sorting data

print(f"OIL 10: \n{oil_series.sort_values().iloc[:10]}")
print(f"OIL 10, sort index: \n{oil_series.sort_values().iloc[:10].sort_index(ascending=False)}")

mask = (oil_series.index.isin(dates)) & (oil_series <=40)
print(f"OIL - specified dates, val. less than 40:: {oil_series[mask]}")
#%%