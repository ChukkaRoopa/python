'''
dictionary - it is an unordered collection of data values, which holds a key: value pair
it can also be created by build-in function - dict()
'''

dict1 = {}
print("Empty dictionary: ", dict1)

dict2 = {1 : "leo", 2: "bunny"}
print("Dictionary with the use of integer keys: ", dict2)

dict3 = {"Name":"Roopa", 1:[1,2,3,4]}
print("Dictionary with the use of mixed keys: ", dict3)

dict4 = dict({1 : "leo", 2: "bunny"})
print("dictionary with dict() function: ", dict4)

dict5 = dict([(1, "Leo"), (2, "bunny")])
print("Dictionary with each item as a pair: ", dict5)

# Accessing key-value from dictionary
dict = {1 : "leo", 2: "bunny"}
print("Accessing element using a key: ", dict[2])
print("Accessing element using a key: ", dict.get(1))

dict = {"Name":"Roopa", "a":[1,2,3,4]}
print("Accessing element using a key: ", dict.get("a"))