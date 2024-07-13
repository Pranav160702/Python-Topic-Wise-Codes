class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"    
        



print(Person('Pranav',23))
print(Person('Akash', 22))


