#%%
import numpy as np

rng = np.random.default_rng(66)

# Inventory individual prices
prices = (rng.random(10) * 10).round(2)
print(f"Prices: {prices}")

# Inventory
inventory = rng.integers(1, 100, 10)
print(f"Inventory: {inventory}")
print(inventory.mean())
print(inventory.sum())
print(inventory.min())
# Standard deviation
print(inventory.std().round())

print(f"Total values of given products in stock: {prices * inventory}")
print(f"Total value of inventory: {(prices * inventory).sum()}")
print(f"Mean value of inventory: {(prices * inventory).mean()}")
print((prices * inventory).min())

print(f"INDEX of the most valuable product: {(prices * inventory).argmax()}")
print(f"Product with the lowest amount in stock: {inventory.min()}")


# Reshape array
prices_2d = prices.reshape(5,2)
# Calculate sum of columns (axis=0) and average/mean of rows (axis=1)
print(prices_2d.sum(axis=0))
print(prices_2d.mean(axis=1))

# Inventory - np.median() and percentile()
product_value = inventory * prices

reshaped_product_value = product_value.reshape(2, 5)
print(f"Reshaped: {reshaped_product_value}")

print(f"Median: {np.median(reshaped_product_value).round(3)}")
print(f"Percentile: {np.percentile(reshaped_product_value, 10)}")


#%%