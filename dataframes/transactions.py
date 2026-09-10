#%%
import pandas as pd

trans = pd.read_csv("../csv/transactions.csv")
print(trans.count())

print(">> Transactions info: ")
trans.info()

print(">> Transactions describe: ")
print(trans.describe(include="all"))
print(f">>> Missing data?: \n{trans.isna().sum()}")


# Ex
# Copy of DataFrames that excludes row 1 January 13, and include 'store_nbr" and "transactions":
print(trans.head())
updated_trans = trans.loc[1:, ["store_nbr", "transactions"]]
print(updated_trans.iloc[:5])

# Unique store numbers
print(">>> Unique")
print(trans.loc[:, "store_nbr"].nunique())

# Total in millions
print(f">>> Total trans: {updated_trans.loc[0:, "transactions"].sum()}")

#%%