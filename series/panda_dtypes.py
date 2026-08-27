#%%
import pandas as pd

# Panda data types

# NUMERIC:
# boolean
# int64 (default)
# float64 (default)

# OBJECT / TEXT:
# object
# string
# category ( Maps categorical data to a numeric array for efficiency! )


# TIME SERIES: 
# datetime64 (A single moment in time; April 5, 2020, 18:00:00 PM)
# timedata ( Duration btw two dates or times)
# period ( A span of time ; a day, a week...)

sample_series = pd.Series([11,0,-4,0,10,8,50,0], name="Sample-series")

print("Sample series range [2:5]")
print(sample_series[2:5])
print(f"--> : {sample_series.index}")
print(f"--> : {sample_series.size}")

sample_index = [10,20,30,40,50,60]
sales = [110,0,80,150,80,280]

object_type_sample = pd.Series(sales, index=sample_index, dtype=object)

print("Converting pd series to diff types:")
print(f"--> float : {sample_series.astype("float")}")
print(f"--> boolean: {sample_series.astype("bool")}")
print(f"--> string: {sample_series.astype("string")}")
print(f"--> object + custom indexes: {object_type_sample}")

# Items serve as a custom index in sales_series
items = ["bananas","cashew","cookies","oil","potatoes","flour"]

sales_series = pd.Series(sales, index=items, name="Grocery sales")
print(f"sales_series: {sales_series}")
print(f"sales_series - cookies: {sales_series["cookies"]}")

# Slicing custom indices - makes stop point INCLUSIVE
print("sales_series custom range:")
print(sales_series["cashew":"potatoes"])



#%%