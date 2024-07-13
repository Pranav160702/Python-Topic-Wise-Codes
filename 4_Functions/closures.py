def outer(a, b):

    sum_ = a + b

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You have just called a Closure..."
    
    return inner

func = outer(4,5)
func()
# print(func.__closure__)