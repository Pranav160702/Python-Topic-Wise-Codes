def wrapper(func):
    def inner(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return inner


def add(a,b,c):
    return a+b+c

def greet(name):
    return "Hello "+name

@wrapper
def add(a,b,c):
    return a+b+c
# add = wrapper(add)

print(add(1,2,3))

