#%%
import numpy as np
import pandas as pd


string_series = pd.Series(["day 1","day 2","day 3","day 4","day 4",])

apply_lambda = string_series.apply(lambda x: x[-1])
print(f"apply lambda: \n{apply_lambda }")

def search(string, looking_for):
 if looking_for in string:
  return "Found!"
 return "- - -"

print(string_series.apply(search, args="4"))

# Using where() !!! use of  ~
string_series.where(string_series.str.contains("2"), "---").where(~string_series.str.contains("2"), "Got it!")

pd.Series(np.where(string_series.str.contains("3"), "YES", "Nothing!"))

# Ex: Output Adult if age more or equal 18, otherwise Teen
ages = pd.Series([16, 21, 15, 25, 14, 19, 22, 17, 13, 20])
adult_ages = ages.where(ages >= 18, "Adult")
result = adult_ages.where(~(ages < 18), "Teen")
print(result)

# Apply and Where - working with oil.csv file 
oil_including_nan = pd.read_csv("../csv/oil.csv")
oil_including_nan_array = np.array(oil_including_nan["dcoilwtico"].iloc[500:800])
oil_including_nan_series = pd.Series(oil_including_nan_array, name="All Items Oil Prices")
oil_including_nan_series.columns = ["transaction_date", "oil_value"]

dates = np.array(oil_including_nan["date"].iloc[500:800])
oil_including_nan_series.index = dates
print(f"oil_including_nan_series \n{oil_including_nan_series}")

# Output Buy if price is less than 90th percentile and Wait if it is higher or equal
p90 = oil_including_nan_series.quantile(0.9)

def buy_or_wait(price, threshold):
 if pd.isna(price) or price >= threshold:
  return 'Wait' 
 return 'Buy'

result_buy_or_wait = oil_including_nan_series.iloc[50:].apply(buy_or_wait, threshold=p90)
print(f">>> Buy or Wait: \n{result_buy_or_wait}")

# Also using lambda:
oil_including_nan_series.apply(lambda x: "Buy" if x < oil_including_nan_series.quantile(.9) else "Wait")

# Multiply price by .9 if date = 2016-12-23 or 2017-05-10 and by 1.1 for all the other
print("---->>>")
oil_price_increase = np.where(oil_including_nan_series.index.isin(['2016-12-23', '2017-05-10']),
oil_including_nan_series * .9,
oil_including_nan_series * 1.1)
print(oil_price_increase)


 # Create df out of oil series
df = pd.DataFrame(oil_including_nan_series)
df["new_price"] = np.where(oil_including_nan_series.index.isin(['2016-12-23', '2017-05-10']),
oil_including_nan_series * .9,
oil_including_nan_series * 1.1)

print(df)


#%%