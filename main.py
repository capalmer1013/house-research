import pandas as pd

csv_filename = "redfin_2023-02-16-16-44-41.csv"
houses = pd.read_csv(csv_filename)
print(houses)
print(houses.dtypes)
print(houses.info())