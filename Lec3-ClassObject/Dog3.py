# Python3 program to show that the variables with a value assigned in the class declaration, are
#       class variables (aka global variables) and variables inside the __init__( ) are instance variables,
#       variables inside methods are local variables

# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'  # global variable!!!

    # The __init__ method or constructor
    # variables inside here are instance variable (belongs to the created objects)
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color

    # Objects of Dog class


Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class name also
print("\nAccessing class variable using class name")
print(Dog.animal)
print("change Dog.animal = stuff animal")
Dog.animal = 'stuff animal'
print("now Dog.animal is", Dog.animal, "address is ", id(Dog.animal))
print("Buzo is now changed to  ", Buzo.animal, "address is ", id(Buzo.animal))

print("change ROger to a "'real animal', "address before the change is ", id(Rodger.animal))
Rodger.animal= 'real animal'
print("Rodger is a ", Rodger.animal, "address is also changed....", id(Rodger.animal))

print("The Dog class still has ",Dog.animal)


