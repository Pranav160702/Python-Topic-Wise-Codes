with open('14_File Handling/exchange_rates.csv') as f:
    header = next(f)

    for row in f:
        row = row.strip()
        date, value_str = row[:2].split(',')

        print(date, value_str)

