#%%
import pandas as pd

oil = pd.read_csv("../csv/oil.csv")

oil.columns = ["date", "price"]

oil.head()
oil[["price", "date"]].loc[:20]

# Specifying rows and columnns to display
oil.iloc[:5, [1]]

# Series
oil.loc[:10, "date"]
# DataFrames
oil.loc[:10, ["date"]]

oil["new_price"] = oil["price"] * 1.2
print(oil.head())

# By dropping column 'inplace' it cannot be retrieved other than reading source(file) again !


# oil_new_price = oil.drop("price", axis=1) 
oil_new_price = oil.drop(2, axis=0) 
print(oil_new_price.head())

# In order to reset index to original oil df, reassigning is needed, or 'inplace=True'
oil_new_price_reset = oil_new_price.reset_index()
print(f"Reset: \n{oil_new_price_reset.head()}")

# 
print("mean() after filling values with 0: !")

print(oil.loc[:, "price"].fillna(0).mean())

print("mean() after calculating known values mean first: !")
print(oil.loc[:, "price"].fillna(oil.loc[:, "price"].mean()).mean())

# Filtering DataFrames
oil["benchmark"] = 107
# print(oil)
# oil.describe()

print(">>> Only oil > benchmark:")
oil.loc[oil["price"] > oil["benchmark"]]

condition_mask = ((oil["price"] > oil["benchmark"]) & (oil["date"].str[:4] == "2014"))
print(">>> Using condition mask ( on price and date): ")
print(oil[condition_mask])

print(f"> > > Price more than benchmark using query: {oil.query("price > benchmark")}!")


#%%