#%%
import pandas as pd

premier_league = pd.read_excel("../csv/premier_league_games.xlsx")

# premier_league.assign(avg_team_goals = premier_league.groupby(["HomeTeam"])["HomeGoals"].transform("mean"))

 #--- Assigning multiple columns - avg_team_goals and difference(this shows how HomeTeams perform comparing HomeGoals with the team average goals)
premier = premier_league.assign(avg_team_goals = premier_league.groupby(["HomeTeam"])["HomeGoals"].transform("mean"), difference = lambda x: x["HomeGoals"] - x["avg_team_goals"])


premier.groupby(["HomeTeam", "AwayTeam"]).agg({"difference" : "mean"}).sort_values("difference", ascending=False)

#--- Additional query tot compare particular data
premier.query("HomeTeam == 'Chelsea' and AwayTeam == 'Queens Park Rangers'")


#--- TRANSACTIONS

trans = pd.read_csv("../csv/transactions.csv")

#--- Renaming columns
trans = trans.rename(columns={"transactions": "transaction_count", "store_nbr": "store_number"}).reindex(labels=["date", "transaction_count", "store_number"], axis=1)

#--- datetime for month and week
trans["date"] = trans["date"].astype("datetime64[ns]")
trans["month"] = trans["date"].dt.month
trans["day_of_the_week"] = trans["date"].dt.dayofweek

#--- Asssigning additional columns: 
trans = trans.assign(pct_to_target = trans["transaction_count"] / 2500)
trans = trans.assign(met_target = trans["pct_to_target"] >= 1)
trans["bonus_payable"] = trans["met_target"] * 100

trans.query("store_number == 25").groupby(["day_of_the_week"]).agg({"transaction_count": "mean"})

# --- Average store transactions for each store
trans.assign(avg_store_transactions = (trans.groupby(["store_number", "day_of_the_week"])["transaction_count"].transform("mean")), difference = (lambda x: x["transaction_count"] - x["avg_store_transactions"]))


# print(trans.head())

#%%
