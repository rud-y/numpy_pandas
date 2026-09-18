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
print(f">>> Trans all: \n{trans.head()}")
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

# Check duplicated transactions from 1000 to 1100th
print(f">> Check duplicated trans : \n{trans.loc[1000:1100, "transactions"].duplicated()}")

# Sorting df
print(f">>> Sort trans by transactions, descending: \n{trans.sort_values("transactions", ascending=False)}")

# axis=1 - Reverses column order
print(f">>> Sort index of trans: \n{trans.sort_index(ascending=False, axis=1)}")

# print(trans.tail())

print(" = = = = =")
# print(trans.sort_values(['month', 'transactions'], ascending=[False, True]))

# Sum of five highest transactions 
five_highest_transactions_sum = trans.sort_values('transactions', ascending=False).head()

print(five_highest_transactions_sum)

# Sort dataset by date ( earliest to most recent ) but the highest 
# transactions first and lowest last
sorted_transactions = trans.sort_values(['date', 'transactions'], ascending=[True, False])
print(f">>> Sorted transactions(date and transactions): \n{sorted_transactions}")

print(trans.sort_index(ascending=False, axis=1))

# Renaming columns
trans = trans.rename(columns={"transactions": "transaction_count", "store_nbr": "store_number"}).reindex(labels=["date", "transaction_count", "store_number"], axis=1)

# Task
# Create pct_to_target - new column that divides transaction_count by 2500
# met_target - new column that is type boolean and returns True if the pct_to_target is 1 or more, else False

trans = trans.assign(pct_to_target = trans["transaction_count"] / 2500)

trans = trans.assign(met_target = trans["pct_to_target"] >= 1)

trans["bonus_payable"] = trans["met_target"] * 100

# Sum of the bonuses paid
print(f">>> Sum of bonuses: \n{trans["bonus_payable"].sum()}")

# dt for month, week
trans["date"] = trans["date"].astype("datetime64[ns]")
trans["month"] = trans["date"].dt.month
trans["day_of_the_week"] = trans["date"].dt.dayofweek

print(trans.head())



#%%