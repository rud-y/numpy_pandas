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





#%%