#%%
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style("darkgrid")
oil = pd.read_csv("../csv/oil.csv")

oil.astype({"date": "datetime64[ns]"}).set_index("date").loc["2013":"2014"].plot()
oil.head()

oil.set_index(oil["date"].astype("datetime64[ns]")).plot(title="Oil Prices 2013-2017", xlabel="Date", ylabel="Price in USD", c="Black")


#%%