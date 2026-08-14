#%%
import numpy as np

town_a_ages = np.array([25, 45, 70, 34, 58])
town_b_ages = np.array([30, 55, 65, 40, 60])

age_differences = np.abs(town_a_ages - town_b_ages)
print(f"Age diff between corresponding ages: {age_differences}")

total_plus_five = town_a_ages + 5
print(f"town a ages PLUS 5 : {total_plus_five}")

#---

sales_array = np.array([0, 50, 0, 4, 55, 1020, 199, 0, 4, 800])
sales_without_zero_values = sales_array[sales_array != 0]
print(sales_array)
print(f"NO ZERO VALUES: {sales_without_zero_values}")

print(f"{sales_array[(sales_array == 4) | (sales_array > 100)]}")
print(f"Sales more than 0 less than 100: {sales_array[(sales_array > 0) & (sales_array < 100)]}")

# Boolean Mask !
mask = (sales_array > 30) & (sales_array < 200)
using_mask = sales_array[mask]
print(f"Sales between 50-200 using 'mask': {using_mask}")

# Filter products based on values in corresponding sales
sales_a = np.array([0, 50, 0, 4, 55, 1020])
product_a = np.array(["fish","vegetables","fruit","yougurt","cornflakes","milk"])
non_zero_products = product_a[sales_a > 0]
print(f"Products with sales more than 0: {non_zero_products}")


# Modify array values
my_array = np.arange(20)
print(f"Modulo - even numbers: {my_array[my_array % 2 == 0]}")

even_odd = np.array(['even', 'odd'] * 10)

my_array[even_odd != 'odd'] = 0
print(f"my_array[even_odd == 'odd'] = 0 -> {my_array}")


# Exer: Filter products with price greater than 20
# Shipping_cost_array - if price > 20 then no shipping fee, otherwise it is 5
products = np.array(["turkey", "salad", "gourment mix", "pepsi", "coffee", "specialty oatcakes box"])
prices = np.array([34.99, 6.99, 20.99, 4.99, 9.99, 22.99])

fancy_specials_mask = (prices > 20) | (products == 'coffee')
np.where(prices > 20, 0, 5)

print(f"Fancy specials: {products[fancy_specials_mask]}")
print(f"Shipping costs: {np.where(prices > 20, 0, 5)}")


#%%