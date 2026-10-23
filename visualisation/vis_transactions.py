#%%
import pandas as pd
import seaborn as sns
import matplotlib

trans = pd.read_csv("../csv/transactions.csv", parse_dates=["date"])

# trans.query("store_nbr == 10").set_index("date").loc["2013-01", "transactions"].plot()
transactions_store_10 = trans.loc[trans["store_nbr"] == 10, ["date", "transactions"]]
transactions_store_10.head()

# transactions_store_10.plot(x="date", y="transactions")

#--- Chart styles
trans.query("store_nbr in [44, 49] and date.dt.year == 2015").pivot_table(index="date", columns="store_nbr").droplevel(0, axis=1).plot(xlabel="Date", ylabel="Transaction Amount", cmap="tab10", alpha=.6, style=["-","--"])

#--- Color samples:
# color=["green","red"]
# cmap="viridis"
# cmap="tab10" ...


#--- Chart for store nbr 45
# transactions_store_45 = trans.loc[trans["store_nbr"] == 45, ["date", "transactions"]]


#---- Legends & Gridlines ---- seaborn & matplotlib ... 
#--- More on: https://matplotlib.org/stable/gallery/style_sheets/

sns.set_style("darkgrid")
matplotlib.style.use("fivethirtyeight")

trans.query("store_nbr in [44, 49] and date.dt.year == 2015").pivot_table(index="date", columns="store_nbr").droplevel(0, axis=1).plot(xlabel="Date", ylabel="Transactions Daily").legend(bbox_to_anchor=(1,1))

# .legend(bbox_to_anchor=(1,1))
# .legend(loc="top left")





#%%