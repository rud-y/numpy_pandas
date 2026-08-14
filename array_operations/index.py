#%%
import numpy as np   

rng = np.random.default_rng(616)

inventory = rng.integers(0, 100, 11)
print(inventory - 24)

inventory_float = (inventory / 2)

inv = inventory.astype('float64')
print(f"Inventory --- {inventory}")


price = (rng.random(11) * 11).round(2)

print(f" price per items random:  {price}")
print(f" Inventory prices:  {price * inventory}")

sum = (price * inventory).sum()
print(f"Sum --- {sum}")

# List
inventory_list = inventory.tolist()
print(inventory_list)

#  Cannot do: inventory_list + 2 

new_inventory = []

for x in inventory_list:
 new_inventory.append(x+2)

print(f" new_inventory: {new_inventory}")
# %%
