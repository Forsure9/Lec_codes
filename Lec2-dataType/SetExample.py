"""
 Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements.
 The order of elements in a set is undefined though it may consist of various elements.

"""

# Python program to demonstrate  Creation of Set in Python

# Creating a Set
set1 = set()
print("Initial blank Set: ")
print(set1)

# Creating a Set with the use of a String
set1 = set("COMP2150 python")
print("\nSet with the use of String: (disordered...) ")
print(set1)

# Creating a Set with the use of a List
set1 = set(["North", "East", "South" ,"West","East", "East"])
print("\nSet with the use of List: 'disordered...' ")
print(set1)

# Creating a Set with a mixed type of values (Having numbers and strings)
set1 = set([1, 2, 'North', 4, 'East', 6, 'South',33,77])
print("\nSet with the use of Mixed Values: 'disordered' ")
print(set1)