
'''
A class is a user-defined blueprint or prototype from which objects are created.
  Classes provide a means of bundling data and functionality together.
  Creating a new class creates a new type of object, allowing new instances of that type to be made.
  Each class instance (object of the class) can have attributes attached to it for maintaining its state.

  Class instances can also have methods (defined by their class) for modifying their state.

Class creates a user-defined data structure,
        which holds its own data members and member functions,
        which can be accessed and used by creating an instance of that class (instantiaion).
A class is like a blueprint for an object.

Some points on Python class:
Classes are created by keyword class.
    Attributes are the variables (data) that belong to a class.
    Attributes are always public and can be accessed using the dot (.) operator.
Example: following program
    Dog.attr1
    Dog.attr2
'''

class Dog:
    # A simple class name Dog
    # class attributes (aka global variables)
    attr1 = "mammal"  # state/attributes
    attr2 = "dog"

    # A sample method
    def fun(self):
        sound = 'barking'  # local variable inside fun()
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
        print("I speak by", sound)


# Object instantiation, create (instantiate) an object called rocky


rocky = Dog()    # rocky is a reference variable (address of the object "rocky")
snoopy = Dog()

# Accessing class attributes and method through objects (using the " . " )
print(rocky.attr1)
rocky.fun()
# print the same thing, but it is a different object
snoopy.fun()



