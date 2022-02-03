"""
are just like the array (arraylist in java), declared in other languages which is a ordered collection of data.
It is very flexible as the items in a list do not need to be of the same type.

"""


# Python program to demonstrate  Creation of List

# Creating a List
List0 = []
print("Initial blank List: ")
print(List0)

# Creating a List with  # the use of a String
List = ['Start123456789']
print("\nList with the use of String: ")
print(List)

# Creating a List with the use of multiple values
List = ["who", "will", "win", "?"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])

print(" add 'Last' to List")
List.append("last")

print ("extend List0 with List")
List0.extend(List)
print(List0)


# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['what', 'is'], ['your name?'],[12345],['secondLast'],['last']]
print("\nMulti-Dimensional List: ")
print(List)
print(List[-1])
print('length of List: ',len(List))

# loop through exmples
