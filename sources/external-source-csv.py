#%%
import numpy as np
import pandas as pd

# Create dataFrame from oil.csv ( drop missing values)
oil = pd.read_csv("../csv/oil.csv").dropna()

# Read csc file including NaN/empty values, rename columns, fill missing vals with 0
oil_including_nan = pd.read_csv("../csv/oil.csv")

oil_including_nan_array = np.array(oil_including_nan["dcoilwtico"].iloc[800:900])
print(f">>> Oil_including_nan_array : {oil_including_nan_array}")

oil_including_nan_series = pd.Series(oil_including_nan_array, name="All Items Oil Prices")

oil_including_nan_series.columns = ["transaction_date", "oil_value"]
print(f">>> Oil Series Count including nan Series :{oil_including_nan_series.count()}")
print(oil_including_nan_series[:10].fillna(0))
print(f">>> Oil Series incl. NaN >>> {oil_including_nan_series}")

# Values for oil prices - 100 items
oil_array = np.array(oil["dcoilwtico"].iloc[800:900])

# Convert np array into Panda series, assign name
oil_series = pd.Series(oil_array, name="Oil Prices")
print(f">>> Oil_series.count() :  {oil_series.count()}")
print(f">>> Oil series 100 items: {oil_series}")

# !!! Extract dates column, set as index !!!
dates = np.array(oil["date"].iloc[800:900])
oil_series.index = dates
oil_including_nan_series.index = dates

print(f">> Oil series after assigned dates as index! :: \n{oil_series[:15]}")
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

my_series = pd.Series([5,10,15,20,25,25], index=["day 1","day 2","day 3","day 4","day 5", "day 6"])

# print(f"my_series -- {my_series == 2}")
print(f">>>Values excluding 10 and 25: {my_series.loc[~my_series.isin([10, 25])]}")

print(f">>>Greater than 15: {my_series.loc[my_series.gt(15)]}")

print(f"Is 15 present: {my_series.isin([15])}")

mask = ((my_series.le(20)) & (my_series > 5))
print(f">>>More than 5 & including 20: {my_series.loc[mask]}")

my_series = my_series.reset_index(drop=True)
print(f"Reset index my_series: \n{my_series}")


# Sorting data
print(f"OIL 10, sorted values:  \n{oil_series.sort_values().iloc[:10]}")
print(f"OIL 10, sorted by index, descending: \n{oil_series.sort_values().iloc[:10].sort_index(ascending=False)}")

mask = (oil_series.index.isin(dates)) & (oil_series <=40)
print(f"OIL - specified dates, val. less than 40:: {oil_series[mask]}")


# Other Series operations
print(f"10% increase: {oil_series * 1.1 + 2}")
print(f"Same result using methods: {oil_series.mul(1.1).add(2).round(1)}")

max_price = oil_series.max()
print(f"Max price: {max_price}")

print("Percentage difference between MAX PRICE  and all other values: ")
print(((oil_series - max_price) / max_price).round(2))


month = oil_series[30:61].index.str[5:7].astype('int')
print(month)
print(f"Extract months from the index(converted to Series) for 30 entries: \n{pd.Series(month)}")

#
print(f"Unique: {my_series.unique()}")
print(oil_series.value_counts())


# Exercise
# Convert Text series into 2 columns, age_group(eg. 'Adult') and age.
# Make age of type integer
age_data = pd.Series(['Adult 25', 'Child 12', 'Adult 64', 'Teen 17', 'Adult 45'])

split_data = age_data.str.split(' ', expand=True)

split_data.columns = ["age_group", "age"]

split_data["age"] = split_data["age"].astype(int)
print(split_data)
print(split_data.dtypes)

# Calculate oil series sum and mean prices in March
# mean
oil_series_mean_march = oil_series[oil_series.index.str[5:7] == "03"].mean().round(3)
print(oil_series_mean_march)

# sum
oil_series_sum_march = oil_series[oil_series.index.str[5:7] == "03"].sum().round(3)
print(oil_series_sum_march)

# Number of oil transactions in April and May
april_may_oil_trans = oil_series[oil_series.index.str[5:7].isin(["04", "06"])]
mask_between_46_48 = (april_may_oil_trans.ge(46) & april_may_oil_trans.le(48))

print(f">> April AND June prices range 46-48 count : \n{april_may_oil_trans[mask_between_46_48].count()}")

print(f">> April AND June COUNT: {april_may_oil_trans.count()}")

# 10 and 90 percentile values
print(oil_series.quantile([0.1, 0.9]))


# -----
# Missing Data and Handling missing data 
print(oil_including_nan_series.isna())
print(f">>> Mean of isna : {oil_including_nan_series.isna().mean()}")

sample_series = pd.Series([pd.NA] * 10)
sample_series = sample_series.astype("Int64")
print(sample_series.isna().sum())
print(f">>> Value_counts including <NA> : \n{sample_series.value_counts(dropna=False)}")

sample_series2 = pd.Series(range(8))
sample_series2.loc[4:6] = pd.NA
print(f">>> Sample_series2 : {sample_series2}")
print(sample_series2.isna().count())
print(f">> Value counts: \n{sample_series2.value_counts(dropna=False)}")
print(f">> Fill missing values with mean() : \n{sample_series2.fillna(sample_series2.mean())}")

print(f">> Number of undefined values: {sample_series2.isna().sum()}")
print(">> Drop NA from the Series: ")
print(sample_series2.dropna().reset_index(drop=True))


# Missing Data ... oil_including_nan_series

all_entries_oil_series = oil_including_nan_series.where(~oil_including_nan_series.isin([47.83, 51.44]), np.nan)

print("Number of all_entries_oil_series / and entries from 30 - 51: ")
print(all_entries_oil_series.isna().sum())
print(all_entries_oil_series.iloc[30:50])

print(f">>> Fill missing entries with median: {all_entries_oil_series.fillna(all_entries_oil_series.median()).iloc[30:50]}")


#%%