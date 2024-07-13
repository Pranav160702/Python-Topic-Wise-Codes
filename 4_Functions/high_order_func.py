def choose_operator(name):

    # def add(a,b):
    #     return a + b

    # def mul(a,b):
    #     return a * b

    # def power(a , n):
    #     if n == 0:
    #         return 1
    #     else:
    #         return a ** n
        

    if name == "add":
        return lambda a, b : a + b
    elif name == "mul":
        return lambda a, b : a * b
    elif name == "power":
        return lambda a, n : a **n
    

op = choose_operator('mul')
print(op)
print(op(2,3))













# def greet(name):
#     return f"Hello {name}"

# # print(add(2,3),greet("Pranav"))
# def apply_fun(func, *args):
#     result = func(*args)
#     return result

# print(apply_fun(add,2,3))
# print(apply_fun(greet,"Pranav"))














# def say_hello(first_name, last_name):
# 	def assemble_name():
# 		return ' '.join([first_name, last_name])
# 	return ' '.join(['Hello', assemble_name(), '!'])


# print(say_hello('Pranav','jadhav'))