# Class Example 

class DemoClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

person1 = DemoClass("Pranav",22)
person1.display()
person2 = DemoClass("Rajesh",28)
person2.display()
