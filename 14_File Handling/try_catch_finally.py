f = open('14_File Handling/exchange_rates.csv')
try: 
    for line in f:
        print(line)
        raise ValueError('Forcing an Exception')
finally:
    print("Closing File....")
    f.close()