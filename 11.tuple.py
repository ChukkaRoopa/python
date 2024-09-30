# Tuple - tuple is also an ordered collection of data, the only diff b/w list and tuple is tuple is immutable
# i.e tuples cannot be modified after they are created. parenthesis ()
tuple1 = ()
print('Empty tuple: ', tuple1)

tuple2 = ("Roopa", "Age")
print("Tuple with the use of a string: ", tuple2)

list3 = ["Roopa", "Age"]
tuple3 = tuple(list3)
print("Tuple using list: ", tuple3)

tuple4 = tuple("Roopa")
print("Tuple using functions: ", tuple4)

tuple5 = (1, 2, 3, 4)
tuple6 = ("Bunny", "Leo")
tuple7 = (tuple5, tuple6)
print("Tuple with nested tuples: ", tuple7)

# tuple with repetition
tuple1 = ("Leo",) * 3
print("Tuple with repetition: ", tuple1)

# creating tuple with the use of loop
tuple1 = ("Charlie", "Leo", "Bunny", "Blacky")
for i in range(6):
    tuple1 = (tuple1)
    print(tuple1)

# Tuple operations
# Accessing elements of a tuple
print("Accessing elements of a tuple: ", tuple7[1][1])

# tuple unpacking
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

# concatenation of tuples
a = ("Banana", "Grapes", "Orange")
b = ("Yellow", "Black", "orange")
tuple1 = a + b
print("concatenation of tuples: ", tuple1)

# slicing
print("sicing of tuples: ",tuple1[::-1])

# deleting a tuple
del tuple1

# Tuple methods
tuple1 = ("Charlie", "Leo", "Bunny", "Blacky","Leo")
print("count: ", tuple1.count("Leo"))

# index() method - index(element, start, end)
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2) 
print("index() method: ", tuple1.index(2))

print("index() method: ", tuple1.index(2,6))