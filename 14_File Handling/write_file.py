# Writing text files
with open('demo.txt','w') as f:
    f.write('Hello, This is Pranav!')
    f.write('\nComputer Engineer!')
    f.write('\nI am from India!')


with open('demo.txt','r') as f:
    print(f.readline())

print(help(read))


# f = open('test.csv', 'w')
# f.write("Pranav\n")

# f.write('12345\n')

# f.close()

# with open('test.csv') as f:
#     print(f.read())