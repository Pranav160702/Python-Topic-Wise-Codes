import csv 

with open('15_Modules/csv_modules.py/exchange_rates.csv') as f:
    reader = csv.reader(
        f, delimiter=',', 
        # quotechar="'", 
        escapechar="\\",
        quoting=csv.QUOTE_MINIMAL
    )
    for row in reader:
        print(row)