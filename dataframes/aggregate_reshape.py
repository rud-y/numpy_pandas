#%%
import pandas as pd

premier_league = pd.read_excel("../csv/premier_league_games_full.xlsx")
# premier_league.head()

# premier_league.groupby(["season", "HomeTeam"], as_index=False)[["HomeGoals"]].sum()
premier_league.groupby(["season", "HomeTeam"], as_index=False)[["HomeGoals"]].sum().query("HomeTeam == 'West Ham United'")
# premier_league.head()



# --- TRANSACTIONS ---
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
trans.head()

# Group transactions to include store number and group by month(ascending) and by total value of transactions (descending)
trans.groupby(["store_number","month"])[["transaction_count"]].sum().sort_values(["month","transaction_count"], ascending=[True, False])



#%%