# pass statement example
# pass is a null operation, it does nothing when executed   
# it is used as a placeholder when a statement is required syntactically but no execution of code
# is necessary

for letter in 'Python':
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

# example 1
for i in range(5):
    pass
# example 2
if True:
    pass
# example 3
def my_function():
    pass
# example 4
try:
    pass
except Exception as e:
    pass
# example 5
if True:
    pass
else:
    pass
# example 6
for i in range(5):
    if i == 3:
        pass
# example 7
while True:
    pass
# example 8
class MyClass:
    pass
    
