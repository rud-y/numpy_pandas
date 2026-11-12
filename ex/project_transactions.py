#%%
import numpy as np
import pandas as pd

proj_transactions = pd.read_csv('../csv/project_transactions.csv')
proj_transactions.head()


proj_transactions.isna().sum()
proj_transactions.info(memory_usage="deep")

proj_transactions["household_key"].nunique()
proj_transactions["PRODUCT_ID"].nunique()

#---- Column capturing total discount ( RETAIL_DISC total and COUPON_DISC total)
#---- Get the percentage of discount, should be positive

print(">>> >>> >>>")
proj_transactions = (proj_transactions.assign(total_discount = proj_transactions["RETAIL_DISC"] + proj_transactions["COUPON_DISC"], percentage_disc = (lambda x: (x["total_discount"] / x["SALES_VALUE"]).abs())).drop(["RETAIL_DISC", "COUPON_DISC", "COUPON_MATCH_DISC"], axis=1))

# proj_transactions.head()

#--- Using .where() to cap values below 0 to 0 and above 1 to1
proj_transactions["percentage_disc"] = (proj_transactions["percentage_disc"].where(proj_transactions["percentage_disc"] < 1, 1.0).where(proj_transactions["percentage_disc"] > 0, 0))

print(">>> proj_transactions >>> ")
print(proj_transactions.head())

#--- Total discount
print(proj_transactions["total_discount"].sum())

#--- OVERALLL percent discount
proj_transactions["SALES_VALUE"] = proj_transactions["SALES_VALUE"].astype("int64")
proj_transactions.info(memory_usage="deep")

total_perc_disc = proj_transactions["total_discount"].sum() / proj_transactions["SALES_VALUE"].sum()
print(">>> total_perc_disc---- ")
print(total_perc_disc)

#--- inf count 
inf_count = np.isinf(proj_transactions["percentage_disc"]).sum()
print(f">>>Number of infinite values: {inf_count}")

#---Mean
print(f">>>Mean of percentage discount: {proj_transactions['percentage_disc'].mean()}")

#--- Max quantity sold
print(f"{proj_transactions['QUANTITY'].max()}")

print(">>> argmax")
print(proj_transactions.loc[proj_transactions["QUANTITY"].idxmax()])

#--- Sales value per basket ( transaction )
proj_transactions["SALES_VALUE"].sum() / proj_transactions["BASKET_ID"].nunique()

#--- Plot distribution of households by total sales value
proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum"}).plot.hist()

#--- Group together Sales_value and Quantity
proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum", "QUANTITY": "sum"}).sort_values("SALES_VALUE", ascending=False).iloc[:10]

top10quantity = proj_transactions.groupby("household_key").agg({"QUANTITY": "sum"}).sort_values("QUANTITY", ascending=False).iloc[:10]

#--- Top 10 households with highest sales 
top10value = proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).iloc[:10]

top10value["SALES_VALUE"].plot.bar()

#--- Top 10 products
# top10products = proj_transactions.groupby(["PRODUCT_ID"]).agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).iloc[:10]

# top10products["SALES_VALUE"].plot.barh()

#%%