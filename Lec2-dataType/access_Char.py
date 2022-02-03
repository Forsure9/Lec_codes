'''
 individual characters of a String can be accessed by using the method of Indexing.
 Indexing allows negative address references to access charactersfrom the back of the String,
    e.g. -1 refers to the last character,
         -2 refers to the second last character and so on.
'''

# Python Program to Access characters of String

s1 = "0123456789"
print("Initial String: ")
print(s1)

# Printing First character
print("First character of String is: ")
print(s1[0])

# Printing Last character
print("Last character of String is: ")
print(s1[-1])
print("Last 4th character of String is: ")
print(s1[-4])