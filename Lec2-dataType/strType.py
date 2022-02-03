'''
 Strings are arrays of bytes representing Unicode characters.
 A string is a collection of one or more characters put in a single quote, double-quote or triple quote.
 In python there is no character data type,
    a character is a string of length one. It is represented by str class.

'''



# Python Program for Creation of String

# Creating a String  with single Quotes
S1 = 'Welcome to comp2150 python 2 !! '
print("String with the use of Single Quotes: ")
print(S1)

# Creating a String
# with double Quotes
s1 = "I'm coding in python"
print("\nString with the use of Double Quotes: ")
print(s1)
print(type(s1))

# Creating a String with triple Quotes
s1 = ''' I'm from triple quotes..you can call me "Python2"  '''
print("\nString with the use of Triple Quotes: ")
print(s1 )
print(type(s1 ))

# Creating String with triple Quotes allows multiple lines
s11 = '''Heaven 
         Can 
         Wait..'''
print("\nCreating a multiline String: ")
print(s11)