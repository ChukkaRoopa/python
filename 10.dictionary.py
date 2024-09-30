'''
dictionary is a data structure that stores values in key-value pairs.
values can be any data type and can be duplicated but keys cannot be duplicated.
Time complexity for creating a dictionary is O(len(dict))
'''

Dict = {1: "Leo", 2: ["Charlie", "Blacky"], "Pet" : "Bunny", 4: [1,2,3,4]}
print(Dict)

empty_dict = {}
print("Empty dictionary: ", empty_dict)

# using dict() function
Dict1 = dict({1 : "Leo", 2: [1,2,3,4]})
print("Dict using dict() function: ", Dict1)

# using each value as a pair
Dict2 = dict([(1, "Charlie"), (2, "Leo")])
print("Dict using each value as a pair: ", Dict2)

# nested dictionaries
nested_dict = {1: "Charlie", 2: [1,2,3,3], 
               3: {"Apple": "Red", "Guava": "Green", "Grapes": "Green"}}
print("Nested dictioary: ", nested_dict)

# Adding elements to a dictionary 
# while adding if key-value pair exists - it gets updated, otherwise new key-value pair is created.
empty_dict[1] = "Grapes"
empty_dict["colour"] = "Green"
empty_dict["Apple"] = "Red"
print("Adding elements: ", empty_dict)

empty_dict["colour"] = "Black"
print("Update elements in the empty_list: ", empty_dict)

empty_dict[3] = {4: "orange", 5: "avacado"}
print("Updating dictionary: ", empty_dict)

# Accessing a value
print("Accessing a value: ",Dict["Pet"])

# Accessing a value using get() method
print("Accessing a valuse using get() method: ",Dict.get(4))

# Accessing elements of a nested dictionary
print("Accessing elements of a nested dictionary: ", nested_dict[3]["Grapes"])

# Deleting elements
del Dict2[1]
print("After deleting element: ", Dict2)

# Operations on dictionaries
dict1 = {1: "Python", 2: "API Testing", 3: "DSA", 4: "SQL"}

dict2 = dict1.copy()
print("Copy: ", dict2)

dict1.clear()
print("Clear dict1: ", dict1)

print(dict2.get(3))
print(dict2.items())
print(dict2.keys())
print(dict2.values())

dict2.pop(4)
print("After removing element: ", dict2)

dict2.popitem()
print("After removing element: ", dict2)

dict2.update({2: "Rest API"})
print("After updating element: ", dict2)

# keys() methods
# Accessing keys using keys() method
dict1 = {1: "Python", 2: "API Testing", 3: "DSA", 4: "SQL"}
print("Accessing keys using keys() method: ",dict1.keys())

# access dict by key
# to access 2nd key
j = 0
for i in dict1:
    if j ==1:
        print("2nd key is: ", i)
    j += 1

# access keys using keys() indexing
print("access keys using key() indexing: ", list(dict1.keys())[1])

# Dictionary Comprehension
keys = ["a", "b","c","d","e"]
values = [1,2,3,4,5]

dict1 = {k:v for k,v in zip(keys, values)}
print(dict1)

# using fromkeys() method
dict1 = dict.fromkeys(range(6), "Apple")
print(dict1)

# example
dict1 = { x: x*4 for x in [1,2,3,4,5]}
print(dict1)

# Example
dict1 = { x.upper():x*4 for x in "Roopa "}
print(dict1)

# example
dict1 = {x:x*2 for x in [1,45,67,82,90,95] if x % 2 == 0 }
print(dict1)