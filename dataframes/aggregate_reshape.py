#%%
import pandas as pd

#### --- TRANSACTIONS --- ###
# --------------------
trans = pd.read_csv("../csv/transactions.csv", parse_dates=["date"])
trans.head()
trans = trans.rename(columns={"transactions": "transaction_count", "store_nbr": "store_number"}).reindex(labels=["date", "transaction_count", "store_number"], axis=1)

trans = trans.assign(pct_to_target = trans["transaction_count"] / 2500)
trans = trans.assign(met_target = trans["pct_to_target"] >= 1)
trans["bonus_payable"] = trans["met_target"] * 100
trans["date"] = trans["date"].astype("datetime64[ns]")
trans["month"] = trans["date"].dt.month
trans["day_of_the_week"] = trans["date"].dt.dayofweek
# trans.head()

### Group transactions to include store number and group by month(ascending) and by total value of transactions (descending):

print(" ==================================")
print(trans.groupby(["store_number","month"])[["transaction_count"]].sum().sort_values(["store_number", "transaction_count"], ascending=[True, False]))


# # # MULTI - INDICES
grouped = trans.groupby(["store_number", "month"]).agg({"transaction_count": ["sum", "mean"]}).sort_values(by=["month", ("transaction_count", "sum")], ascending=[True, False])

print("===========grouped==============")
print(grouped)

# grouped.loc[(42, 2)]
grouped.loc[:, [("transaction_count", "mean")]]
grouped.loc[(3, 1), ("transaction_count", "sum")].sum()


grouped.reset_index().droplevel(0, axis=1)  # This way we lose the first column 'layer' / headers

grouped.droplevel(0, axis=1).reset_index() # By reversing - droplevel first - the column names remain




#%%