#%%
import pandas as pd

retail = pd.read_csv("../csv/retail.csv")

sample_df = retail.sample(5, random_state=85)

print(">>> sample_df:")
print(sample_df)

sample_df.assign(
 onpromotion_flag=sample_df["onpromotion"] > 0,
 family_abbreviation=sample_df["family"].str[:3]
)

print(f">>> Assigned two more cols: \n{sample_df}")

#--- MEMORY USAGE INFO ---
print(">>> Original memory usage  - retail:")
print(sample_df.info(memory_usage="deep"))

sample_df = sample_df.astype({"family": "category"})
print(sample_df["family"].cat.codes)
print(" - - - ")
print(sample_df.loc[:, "family"].value_counts())
print(sample_df.info(memory_usage="deep"))
# print(sample_df)


# ---- Pivot Tables ----

print(f">>> Store_nbr dtyype: \n{retail["store_nbr"].dtype}")

#--- Product family sales for each store ( number 1 to 6 only )
retail[retail["store_nbr"].isin([1,2,3,4,5,6])].pivot_table(index="family", columns="store_nbr", aggfunc=({"sales": ["sum", "mean"], "onpromotion": "max"}))

#--- Heatmap - default value for axis=None : applies gradient accross the whole table - highest values=green, lowest=red

# axis=1 - applied for columns
# axis=0 - rows
retail.pivot_table(index="family", columns="store_nbr", values="sales", aggfunc="sum").style.background_gradient(cmap="RdYlGn", axis=1)





#%%