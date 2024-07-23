import csv

with open('15_Modules/csv_modules.py/exchange_rates.csv') as f:
    reader = csv.reader(f, delimiter=',',quotechar="'")
    for row in reader:
        print(row)
