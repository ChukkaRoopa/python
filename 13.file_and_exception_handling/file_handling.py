# Working in read mode

file1 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r')
# to print each line in the file
for i in file1:
    print(i)

# reading file using file.read() method
file1 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r')
print(file1.read())

# reading file using with statement
with open("/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt") as file:
    data = file.read()
print(data)

# to read certain number of characters
file1 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r')
data = file1.read(7)
print(data)

# we can also split lines while reading
with open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r') as file:
    data = file.readlines()
    for lines in data:
        word = lines.split()
        print(word)

#  Creating a file using write() function
file2 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'w')
file2.write("Hello World")
file2.write("this is the write program")
file2.close()
file2 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r')

# using with statement
with open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'w') as f:
    f.write("Hello World")

# working in append mode
file2 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'a')
file2.write("Hello Roopa")
file2.close()
file2 = open('/Users/roopachukka/Documents/python/13.file_and_exception_handling/example_file.txt', 'r')

