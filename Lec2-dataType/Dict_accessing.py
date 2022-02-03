# Python program to demonstrate accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'COMP', 'number': '2150', 3: 'python'}
print(Dict)
# accessing a element using key
print("Accessing a element using key:")
print(Dict['number'])

# accessing a element using get() method
print("Accessing a element using get:")
print(Dict.get(3))