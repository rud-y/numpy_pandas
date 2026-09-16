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
print(">>> Updated_trans: ")
print(updated_trans.iloc[:5])

# Unique store numbers
print(">>> Unique")
print(trans.loc[:, "store_nbr"].nunique())

# Total in millions
print(f">>> Total trans: {updated_trans.loc[0:, "transactions"].sum()}")


# Percentage of times when oil transactions were over 3000 for store 25 only!
transactions_over_2000 = trans.query("store_nbr == 25 and transactions > 3000")
print(f">>> Store 25 over 2000 transactions: \n{transactions_over_2000}")

# OR

cond_mask = (trans["transactions"] > 3000) & (trans["store_nbr"] == 25)
# Transactions for store 25 - all:
number_of_trans_store25 = trans.loc[trans["store_nbr"] == 25, "transactions"].count()

print("And...filtering non-query: ")
print(trans.loc[cond_mask, "transactions"].count() / trans.loc[trans["store_nbr"] == 25, "transactions"].count())

print(f">>> Sum: \n{trans.loc[cond_mask, "transactions"].sum()}")
#%%