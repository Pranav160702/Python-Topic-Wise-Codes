

# def print_info(name, city, age = 0):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# print_info("Alice", city="New York", age=30)
# # Output: Name: Alice, Age: 30, City: New York

# print_info("Alice", city="New York") #Default value will be use 
# # Output: Name: Alice, Age: 0, City: New York

# print_info(city="New York", "Alice", age=30)
# # SyntaxError: positional argument follows keyword argument

# def greet(*names):
#     for name in names:
#         print(f"Hello, {name}!")

# greet("Alice", "Bob", "Charlie")

# Another Example of Arbitrary Arguments *args

# def calculate_total_cost(*prices):
#     total_cost = 0
#     print(prices)    # Output : (10, 20, 30, 40, 50)           
#     for price in prices:
#         total_cost += price
#     return total_cost

# print(calculate_total_cost(10, 20, 30, 40, 50))  # Output: 150


# def order_summary(order_id, *items):
#     print(f"Order ID: {order_id}")
#     print("Items ordered:")
#     for item in items:
#         print(f"- {item}")

# order_summary(123, "apple", "banana", "cherry")


def print_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")

