'''
Data Types - Data types are the classification or categorization of the data items. It represents the kind of 
value that tells what operations can be performed on a particular data.

Standard build-in data types are:
- numeric
- boolean
- set 
- dictionary
- sequence type - list, string, tuple
- binary types - memoryview, bytearray, bytes

type() - used to check the type of the data
'''


x = "Roopa"  #string
x = 63  #integer
x = 63.9  #float
x = 5j  #complex
x = ["Roopa", "Manohar", "Leo"]  #list
x = ("Roopa", "Manohar", "Leo")  #tuple
x = range(10)  #range
x = {"Name" : "Roopa", "Age" : 23}  #dictionary
x = {"Name", "Age"}  #Set
x = frozenset({"Name", "Age"})  #frozenset
x = True #Boolean
x = b"Roopa" #Bytes
x = bytearray(5)  #bytearray
x = memoryview(bytes(4))  #memoryview
x = None  #None