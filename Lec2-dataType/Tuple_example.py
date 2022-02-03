# Python program to demonstrate creation of tuple

# Creating an empty tuple
Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)

# Creating a Tuple with the use of Strings
Tuple1 = ('Warriors', 'Lakers')
print("\nTuple with the use of String: ")
print(Tuple1)

# Creating a Tuple with the use of list
list1 = [1, 2, 4, 5, 6]
print("Tuple using List: ")
print(tuple(list1))

# Creating a Tuple with the use of built-in function
Tuple1 = tuple('COMP2150')
print("\nTuple with the use of function: ")
print(Tuple1)

# do it without ( )
t1 = 1, 3, 5,
print('single element tuple: ', t1)

# Creating a Tuple with nested tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'wonder')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)