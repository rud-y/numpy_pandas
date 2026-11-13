#%%
from matplotlib import ticker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

proj_transactions = pd.read_csv('../csv/project_transactions.csv')
proj_transactions.head()


proj_transactions.isna().sum()
proj_transactions.info(memory_usage="deep")

proj_transactions["household_key"].nunique()
print(f">>> Unique PRODUCT_IDs : \n{proj_transactions['PRODUCT_ID'].nunique()}")
print(proj_transactions["PRODUCT_ID"].count())

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

#--- OVERALLL percentage discount
proj_transactions["SALES_VALUE"] = proj_transactions["SALES_VALUE"].astype("int64")
proj_transactions.info(memory_usage="deep")

total_perc_disc = proj_transactions["total_discount"].sum() / proj_transactions["SALES_VALUE"].sum()
print(">>> Total percentage discount : ")
print(total_perc_disc)

#--- inf count 
inf_count = np.isinf(proj_transactions["percentage_disc"]).sum()
print(f">>> Number of infinite values: {inf_count}")

#---Mean
print(f">>> Mean of percentage discount: {proj_transactions['percentage_disc'].mean()}")

#--- Max quantity sold
print(f">>> Max quantity sold\n{proj_transactions['QUANTITY'].max()}")

print(">>> argmax")
print(proj_transactions.loc[proj_transactions["QUANTITY"].idxmax()])

#--- Sales value per basket ( transaction )
proj_transactions["SALES_VALUE"].sum() / proj_transactions["BASKET_ID"].nunique()

# #--- Plot distribution of households by total sales value ---
# proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum"}).plot.hist(color="pink", edgecolor="black")

#--- Group together Sales_value and Quantity
proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum", "QUANTITY": "sum"}).sort_values("SALES_VALUE", ascending=False).iloc[:10]

#--- Quantity per household
top10quantity = proj_transactions.groupby("household_key").agg({"QUANTITY": "sum"}).sort_values("QUANTITY", ascending=False).iloc[:10]


#--- Top 10 households with highest sales --- 
top10value = proj_transactions.groupby("household_key").agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).head(12)
print(top10value)

###---
top10value.plot.bar(color="green", edgecolor="darkblue")
plt.title("Top 12 households with highest sales", fontweight="bold", pad=30)
plt.xlabel("Household ID")
plt.ylabel("Sales Value")


#--- Top 10 products sold ( based on SALES_VALUE )---
top10products = proj_transactions.groupby(["PRODUCT_ID"]).agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).head(10)

#--- DataFrame dimensions:
print(top10products.ndim) # 2
print(type(top10products))
print(">>> TOP TEN PRODUCTS IN SALES:")

# top10products["SALES_VALUE"].plot.barh()
print(top10products)

top_10_clean_products = top10products.reset_index()
top_10_clean_products["PRODUCT_ID"] = top_10_clean_products["PRODUCT_ID"].astype(str)

###---
top_10_clean_products.sort_values(by="SALES_VALUE", ascending=False).plot.barh(y="SALES_VALUE", x="PRODUCT_ID", color="steelblue", edgecolor="black")
plt.title("Top 10 Products sold", fontweight="bold", fontsize=15, pad=30)
plt.xlabel("Sales Value")
plt.ylabel("Product ID")


#--- Breakdown of Household with the highest sales (1023): 7 most bought ( or highest QUANTITY) for Product IDs ---
household1023_7_most_sought_after_products = proj_transactions.query("household_key == 1023").groupby(["PRODUCT_ID"]).agg({"QUANTITY": "sum"}).sort_values(by="QUANTITY", ascending=False).head(7)

print(">>>.......")
print(household1023_7_most_sought_after_products)

household1023_7_most_sought_after_products.sort_values(by="QUANTITY", ascending=False).plot.bar(logy=True, figsize=(10, 6))

plt.title("Store with most SALES - Products quantity breakdown", fontweight="bold")
plt.xlabel("Product ID")
plt.ylabel("Quantity sold")

plt.ticklabel_format(style="plain", axis="y")
plt.show()



#%%