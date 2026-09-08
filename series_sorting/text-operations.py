#%%
import numpy as np
import pandas as pd

my_series = pd.Series([5,np.nan ,15,20,25], index=["day 1","day 2","day 3","day 4","day 5",])


print(my_series + 1)
# Add 100 to series also where number nan
my_series2 = my_series.add(100, fill_value=0)
print(my_series2.astype('int'))

print(((my_series2 * my_series2) / 4).astype('int'))


# Text operations
print(f"{"£" + my_series.astype('string')}")
print(f"{my_series.sort_values(ascending=False).astype('string')}")

string_series = pd.Series(["day 1","day 2","day 3","day 4","day 5",])

print(string_series.str.contains('4'))
print(string_series.str.strip('day').astype('int'))

# Numerical operations

transactions = pd.read_csv("../csv/transactions.csv")
transaction_series = pd.Series(transactions["transactions"])

print(f"Transactions : {transaction_series}")
print(f"Transactions_series count : {transaction_series.count()}")
print(f"First 5 transactions_series quantile([.10]) : {transaction_series.iloc[:5].quantile([.10], interpolation="nearest")}")

print(f"Sum transactions >> {transaction_series.sum()}")

# ---
my_series3 = pd.Series([5, 20,15,20,25,25], index=["day 1","day 2","day 3","day 4","day 5", "day 6"])

print(f"Values counts : {my_series3.value_counts(normalize=True)}")
# ---

#%%