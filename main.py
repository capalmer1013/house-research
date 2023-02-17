import pandas as pd

csv_filename = "redfin_2023-02-16-16-44-41.csv"
columns = [
    "SOLD DATE",
    "PROPERTY TYPE",
    "ADDRESS",
    "CITY",
    "PRICE",
    "BEDS",
    "BATHS",
    "SQUARE FEET",
    "LOT SIZE",
    "YEAR BUILT",
    "DAYS ON MARKET",
    "DOLLAR PER SQUARE FEET",
    "HOA/MONTH",
    "URL",
]
houses = pd.read_csv(csv_filename)
print(houses)
print(houses.dtypes)
print(houses.info())
print("===================")
print(houses[columns].info())
