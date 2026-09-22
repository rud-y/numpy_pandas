#%%
import pandas as pd

retail = pd.read_csv("../csv/retail.csv")

sample_df = retail.sample(5, random_state=85)

print(sample_df)

sample_df.assign(
 onpromotion_flag=sample_df["onpromotion"] > 0,
 family_abbreviation=sample_df["family"].str[:3]
)

print(f">>> Assigned two more cols: \n{sample_df}")

print(">>> Original memory usage  - retail:")
print(sample_df.info(memory_usage="deep"))

sample_df = sample_df.astype({"family": "category"})
print(sample_df["family"].cat.codes)
print(" - - - ")
print(sample_df.loc[:, "family"].value_counts())
print(sample_df.info(memory_usage="deep"))
# print(sample_df)




#%%