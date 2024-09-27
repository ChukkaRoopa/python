'''
Sequence data types are ordered collection of similar or different data types.
'''

# strings - string is a collection of one or more characters put in a single quotes, or double or triple quotes
string1 = 'I am a software engineer.'
print("String in single quotes: ", string1)
print(type(string1))

string2 = "I'm a software engineer."
print("String in double quotes: ", string2)

string3 = '''I'm a software engineer who lives in "Vizag".'''
print("String in triple quotes: ", string3)

string4 = '''I'm a software engineer 
            who lives in "Vizag"
            '''
print("creating a multiline string: ", string4)

# Accessing elements of a string
string = "Roopa"
print("First char of a string is: ", string[0])

print("Last char of a string is: ", string[-1])


# list - list is just like arrays, which is an ordered collection of elements. Square brackets []
list1 = []
print("Empty list: ", list1)

list2 = ["Roopa"]
print("list with use of a string: ", list2)

list3 = ["Roopa", "Age", 23]
print("List with multiple values: ",list3)

list4 = [["Roopa", "Age"], "Phone number"]
print("Muliti-dimension list: ", list4)

# Accesing items of a list
print("accessing list items: ", list4[0][1])

print(list4[-2][1])


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

# Accessing elements of a tuple
print("Accessing elements of a tuple: ", tuple7[1][1])