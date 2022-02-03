"""
a Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.
Values in a dictionary can be of any datatype and can be duplicated,
      whereas keys can’t be repeated and must be immutable.
      Dictionary can also be created by the built-in function dict().
      An empty dictionary can be created by just placing it to curly braces{}.

"""

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary with Integer Keys
Dict = {1: 'COMP', 2: '2150', 3: 'python'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'COMP', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary with dict() method
Dict = dict({1: 'COMP', 2: '2150', 3: 'python'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary # with each item as a Pair
Dict = dict([(1, 'COMP'), (2, '2150'), (3, 'python')])
print("\nDictionary with each item as a pair: ")
print(Dict)