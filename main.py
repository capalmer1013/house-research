import datetime as dt
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

import typer

app = typer.Typer()

csv_filename = "redfin_2023-02-16-16-44-41.csv"
columns = [
    "SOLD DATE",
    "PROPERTY TYPE",
    "ADDRESS",
    "PRICE",
    "BEDS",
    "BATHS",
    "SQUARE FEET",
    "LOT SIZE",
    "YEAR BUILT",
    "DOLLAR PER SQUARE FEET",
    "URL",
]
houses = pd.read_csv(csv_filename)

# houses["SOLD DATE 2"] = pd.to_datetime(houses["SOLD DATE"], format="%B-%d-%Y")
houses["DATE SOLD"] = pd.to_datetime(houses["SOLD DATE"], format="%B-%d-%Y")
# houses["new_sold_date"] = dt.datetime.strptime(houses["SOLD DATE"], "%B-%d-%Y").date()
# for each in houses["new_sold_date"]:
#     print(each)

print(houses.info())

@app.command()
def test():
    print(houses)
    print(houses.dtypes)
    print(houses.info())
    print("===================")
    print(houses[columns].info())


@app.command()
def plot():
    houses.plot.scatter(x="DATE SOLD", y="DOLLAR PER SQUARE FEET", c="PRICE")
    plt.gcf().autofmt_xdate()
    # houses
    # scatter_matrix(
    #     houses[
    #         [
    #             "SQUARE FEET",
    #             "PRICE",
    #             "LOT SIZE",
    #             "YEAR BUILT",
    #             "DOLLAR PER SQUARE FEET",
    #             # "new_sold_date",
    #         ]
    #     ],
    #     figsize=(10, 10),
    #     diagonal="kde",
    # )
    plt.show()


if __name__ == "__main__":
    app()
