#%%
from matplotlib import ticker
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales_trans = pd.read_csv('../csv/sales_transactions.csv')
sales_trans.head()


sales_trans.isna().sum()
sales_trans.info(memory_usage="deep")

sales_trans["household_key"].nunique()
print(f">>> Unique PRODUCT_IDs : \n{sales_trans['PRODUCT_ID'].nunique()}")
print(sales_trans["PRODUCT_ID"].count())

#---- Column capturing total discount ( RETAIL_DISC total and COUPON_DISC total)
#---- Get the percentage of discount, should be positive

print(">>> >>> >>>")
sales_trans = (sales_trans.assign(total_discount = sales_trans["RETAIL_DISC"] + sales_trans["COUPON_DISC"], percentage_disc = (lambda x: (x["total_discount"] / x["SALES_VALUE"]).abs())).drop(["RETAIL_DISC", "COUPON_DISC", "COUPON_MATCH_DISC"], axis=1))

# sales_trans.head()

#--- Using .where() to cap values below 0 to 0 and above 1 to1
sales_trans["percentage_disc"] = (sales_trans["percentage_disc"].where(sales_trans["percentage_disc"] < 1, 1.0).where(sales_trans["percentage_disc"] > 0, 0))

print(">>> sales_trans >>> ")
print(sales_trans.head())

#--- Total discount
print(">>> TOTAL DISCOUNT: ")
print(sales_trans["total_discount"].sum())

#--- OVERALLL percentage discount
sales_trans["SALES_VALUE"] = sales_trans["SALES_VALUE"].astype("int64")
sales_trans.info(memory_usage="deep")

total_perc_disc = sales_trans["total_discount"].sum() / sales_trans["SALES_VALUE"].sum()
print(">>> Total percentage discount : ")
print(total_perc_disc)

#--- inf count 
inf_count = np.isinf(sales_trans["percentage_disc"]).sum()
print(f">>> Number of infinite values: {inf_count}")

#---Mean
print(f">>> Mean of percentage discount: {sales_trans['percentage_disc'].mean()}")

#--- Max quantity sold
print(f">>> Max quantity sold\n{sales_trans['QUANTITY'].max()}")

print(">>> argmax")
print(sales_trans.loc[sales_trans["QUANTITY"].idxmax()])

#--- Sales value per basket ( transaction )
sales_trans["SALES_VALUE"].sum() / sales_trans["BASKET_ID"].nunique()

# #--- Plot distribution of households by total sales value ---
# sales_trans.groupby("household_key").agg({"SALES_VALUE": "sum"}).plot.hist(color="pink", edgecolor="black")

#--- Group together Sales_value and Quantity
sales_trans.groupby("household_key").agg({"SALES_VALUE": "sum", "QUANTITY": "sum"}).sort_values("SALES_VALUE", ascending=False).iloc[:10]

#--- Quantity per household
top10quantity = sales_trans.groupby("household_key").agg({"QUANTITY": "sum"}).sort_values("QUANTITY", ascending=False).iloc[:10]


#--- Top 10 households with highest sales --- 
top_10_value = sales_trans.groupby("household_key").agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).head(10)
print(top_10_value)

###---
top_10_value.plot.bar(color="green", edgecolor="darkblue")
plt.title("Top 12 households with highest sales", fontweight="bold", pad=30)
plt.xlabel("Household ID")
plt.ylabel("Sales Value")


#--- Top 10 products sold ( based on SALES_VALUE )---
top10products = sales_trans.groupby(["PRODUCT_ID"]).agg({"SALES_VALUE": "sum"}).sort_values("SALES_VALUE", ascending=False).head(10)

#--- DataFrame dimensions:
print(top10products.ndim) # 2
print(type(top10products))
print(">>> TOP TEN PRODUCTS IN SALES:")

# top10products["SALES_VALUE"].plot.barh()
print(top10products)


#--- Resetting index and changing dtype for PRODUCT_ID to str
top_10_clean_products = top10products.reset_index()
top_10_clean_products["PRODUCT_ID"] = top_10_clean_products["PRODUCT_ID"].astype(str)

###---
top_10_clean_products.sort_values(by="SALES_VALUE", ascending=False).plot.barh(y="SALES_VALUE", x="PRODUCT_ID", color="steelblue", edgecolor="black")
plt.title("Top 10 Products sold", fontweight="bold", fontsize=15, pad=30)
plt.xlabel("Sales Value")
plt.ylabel("Product ID")


# #--- Breakdown of Household with the highest sales (store 1023): 7 most bought ( or highest QUANTITY) for Product IDs ---
household1023_7_most_sought_after_products = sales_trans.query("household_key == 1023").groupby(["PRODUCT_ID"]).agg({"QUANTITY": "sum"}).sort_values(by="QUANTITY", ascending=False).head(7)

plt.title("Store with most SALES - Products quantity breakdown", fontweight="bold")
plt.xlabel("Household")
plt.ylabel("Quantity sold")

print(">>> household1023_7_most_sought_after_products: ")
print(household1023_7_most_sought_after_products)

household1023_7_most_sought_after_products.sort_values(by="QUANTITY", ascending=False).plot.bar()


#--- Find top 10 products total discount / divided by sales value for top 10 products
tot_discount = sales_trans.query("PRODUCT_ID in @top10products.index").loc[:, "total_discount"].sum() / sales_trans.query("PRODUCT_ID in @top10products.index").loc[:, "SALES_VALUE"].sum()

print(f"TOTAL DISCOUNT: \n{tot_discount}")

#--- Check values for total discount and total sales_value
top_ids = top10products.index
print(f"Top_ids:: \n{top_ids}")

# 2. Use .isin() and explicitly match data types to prevent type mismatch bugs
subset = sales_trans[
    sales_trans["PRODUCT_ID"].astype(str).isin(top_ids.astype(str))
]

# 3. Now check how many rows you got
print(f"Number of rows found: {subset.shape[0]}")


products = pd.read_csv('../csv/product.csv')
print(products.head())


#--- Get top 10 products for households in top_10_value table
#--- Query to reference index of top_10_value to filter relevant households
#--- Get count of product_ids, and Get top 10 products
#---  and extract the index to get product numbers


top_household_products = (sales_trans.query("household_key in @top_10_value.index").loc[:, "PRODUCT_ID"]).value_counts().iloc[:10].index

top_household_products

print(">>> PRODUCT_ID in @top_household_products <<< ")
products.query("PRODUCT_ID in @top_household_products")
# products.query("PRODUCT_ID == 981760")

products.query("PRODUCT_ID in @top10products.index")

#%%