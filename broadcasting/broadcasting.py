#%%
import numpy as np
import pandas as pd

test_arr = np.array([[1,2,3], [4,15,6], [1,2,3]])

print(f"array broadcast + 1: {test_arr + np.array([1,10,20])}")
print(f"array broadcast and reshape: {test_arr + np.array([5,10,20])}")

# !!!
print(f"array broadcast and reshape - example 2 !!! : {test_arr[0, :] + test_arr[:, 1].reshape(3, 1)}")


car_types = np.array(["Toyota", "Honda", "Skoda", "Vauxhall", "Mercedes", "Audi", "Hyundai", "Audi", "Range Rover", "Honda", "Skoda", "Kia", "Seat"])
speed = [99,76,87,88,111,86,103,87,94,85,86, 78,77]
speed_array = np.array(speed)

print(f"Avg speed: {speed_array.mean()}")
print(f"Median(mid  value) speed: {np.median(speed_array)}")

# sorted_car_speeds = np.sort(speed_array)
# sorted_car_types = np.sort(car_types)
print(f"car speed : {speed_array}")
print(f"car type sort : {car_types}")

print(f"Speed over 90 ---->>  {car_types[np.where(speed_array > 95)]}")

#%%