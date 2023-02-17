import csv

with open("redfin_2023-02-16-16-44-41.csv") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        print(row)
