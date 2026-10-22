#%%
import pandas as pd

#### --- LEAGUE --- ###
premier_league = pd.read_excel("../csv/premier_league_games.xlsx")
# premier_league.head()

premier_league.groupby(["season", "HomeTeam"], as_index=False)[["HomeGoals"]].sum()
# premier_league.groupby(["season", "HomeTeam"])[["HomeGoals"]].sum().query("HomeTeam == 'West Ham United'")
# premier_league.head()

aggr_premier_league = premier_league.groupby(["season", "HomeTeam"])[["HomeGoals"]].sum()

aggr_premier_league.head()

aggr_premier_league.loc[("2008/2009", "Arsenal"):("2008/2009", "Chelsea")]


# -- agg() method
aggr_premier_league2 = premier_league.groupby(["season", "HomeTeam"]).agg({"HomeGoals": ['sum', 'mean']})
print(f">>> Using .agg() : \n{aggr_premier_league2.head()}")

# Access sum or mean values for HomeGoals,, 
aggr_premier_league2.iloc[4, 0]

print(">>> HOME GOALS: ")
print(aggr_premier_league2.loc[("2010/2011", "HomeGoals", )])

# or sum only
aggr_result = aggr_premier_league2.loc["2010/2011" , ("HomeGoals", "sum")]
print(aggr_result)




#%%