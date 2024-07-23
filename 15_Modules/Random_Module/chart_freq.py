def chart_freq(data):
    
    pad = max([len(str(el[0])) for el in data])
    for k , v in data:
        print(f"{str(k).rjust(pad)}| {'*' * round(v)}")

data_1 =[
    ('abs',25.432),
    ('sdaf',18.085451),
    ('wedx',30.510556),
    ('kgh',35.06065),
    ('fghh',20.02215),
]

chart_freq(data_1)
