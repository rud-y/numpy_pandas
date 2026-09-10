#%%
import pandas as pd

oil = pd.read_csv("../csv/oil.csv")
# print(oil)
print(oil.shape)
print(f">> Dtypes:: \n{oil.dtypes}")
# print(oil.index.max())
# print(f"...oil head() : {oil.head()}")
# print(f"...oil tail() 10: {oil.tail(10)}")
# print(f"...oil sample 10: {oil.sample(10)}")

# print(f"...sample: {oil.sample(10, random_state=1234)}")
print("- - - info :: ")
oil.info()

print("- - - - oil.describe(include='all').round():")
oil_describe = oil.describe(include="all").round()
print(oil_describe)

print(f"- - - oil.describe() without parameters: \n{oil.describe()}")
print(f">>> Missing data?: \n{oil.isna().sum()}")

#%%