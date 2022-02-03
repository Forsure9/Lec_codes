'''
The __init__ method is similar to constructors in C++ and Java.
    Constructors are used to initializing the object’s state.
    Like methods, a constructor also contains a collection of statements(i.e. instructions)
     that are executed at the time of Object creation. For clear code, should keep thes code small and focus on
        initializing attributes only.
     It runs as soon as an object of a class is instantiated.
     The method is useful to do any initialization you want to do with your object.

'''



# A Sample class with init method
class Dog2:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print(self.name,'woof')


p1 = Dog2('Snoopy')
p1.say_hi()

p2 = Dog2('Rocky')
p2.say_hi()