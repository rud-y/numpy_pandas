#%%
import pandas as pd
import seaborn as sns
import matplotlib

sns.set_style("darkgrid")
matplotlib.style.use("ggplot")

trans = pd.read_csv("../../csv/transactions.csv", parse_dates=["date"])

# trans.query("store_nbr == 10").set_index("date").loc["2013-01", "transactions"].plot()
transactions_store_10 = trans.loc[trans["store_nbr"] == 10, ["date", "transactions"]]
transactions_store_10.head()

# transactions_store_10.plot(x="date", y="transactions")

#--- Chart styles

trans.query("store_nbr in [44, 49] and date.dt.year == 2015").pivot_table(index="date", columns="store_nbr").droplevel(0, axis=1).plot(xlabel="Date", ylabel="Transaction Amount", cmap="tab10", alpha=.5, style=["-.","--"])

#--- Color samples:
# color=["green","red"]
# cmap="viridis"
# cmap="tab10" ...


#--- Chart for store nbr 45
# transactions_store_45 = trans.loc[trans["store_nbr"] == 45, ["date", "transactions"]]


#---- Legends & Gridlines ---- seaborn & matplotlib ... 
#--- More on: https://matplotlib.org/stable/gallery/style_sheets/



# transactions_44_49 = trans.query("store_nbr in [44, 49] and date.dt.year == 2015").pivot_table(index="date", columns="store_nbr").droplevel(0, axis=1).plot(xlabel="Date", ylabel="Transactions Daily").legend(bbox_to_anchor=(1,1))

# .legend(bbox_to_anchor=(1,1))
# .legend(loc="top left")


#--- Filter and pivot table : Stores 1 - 4 
stores_1234 = trans.query("store_nbr == [1,2,3,4] and date >= '2014-01-01' and date < '2015-01-01'").pivot_table(index="date", columns="store_nbr").droplevel(0, axis=1)


stores_1234_index = stores_1234.index.astype("datetime64[ns]")
# stores_1234_index

# stores_1234.plot(subplots=True, layout=(2,2), figsize=(8,8), sharey=True, title=["store 1", "store 2", "store 3", "store 4"])


#----- BAR CHARTS ------------------------------------

stores_40s = list(range(40,50))
trans.query("store_nbr in @stores_40s").groupby(["store_nbr"]).agg({"transactions": "sum"}).plot.bar(figsize=(10,10))

# trans.query("store_nbr in @stores_40s and date.dt.month in [1,2,3]").pivot_table(index=trans["date"].dt.month, columns=trans["store_nbr"], values="transactions", aggfunc="sum").apply(lambda x: x * 100 / sum(x), axis=1).plot.bar(stacked=True).legend(bbox_to_anchor=(1,1))

#--- Task Summarize transactions total by store in bar chart. Create Horizontal bar chart ( y axis = month, and x axis = sales), sorted by month
stores_1234_monthly = stores_1234.groupby(stores_1234.index.month).sum()

stores_1234.sum().sort_values(ascending=False).plot.bar(stacked=True)

stores_1234_monthly.sort_index(ascending=False).plot.barh(stacked=
True).legend(bbox_to_anchor=(1,1))

#--- PIE CHARTS-------------------
trans.query("store_nbr in @stores_40s and date.dt.month in [1,2]").groupby("store_nbr").agg({"transactions":"sum"}).plot.pie(y="transactions", title="Stores 40-49").legend(bbox_to_anchor=(1,1))


#--- Scatterplots ---------------
(trans.query("store_nbr in @stores_40s").pivot_table(index=trans["date"].dt.month, columns="store_nbr", values="transactions", aggfunc="sum").plot.scatter(x=44, y=47))





#%%