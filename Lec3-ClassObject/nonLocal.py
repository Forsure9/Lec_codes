'''
https://www.programiz.com/python-programming/global-local-nonlocal-variables
Nonlocal variables are used in nested functions whose local scope is not defined.
This means that the variable can be neither in the local nor the global scope.
Let's see an example of how a nonlocal variable is used in Python.
    use nonlocal keywords to create nonlocal variables.

'''

def outer():
    x = "local"
    print("outter x is ", x, " addr: ", id(x))

    def inner():
        nonlocal x  # comment out this line and see
        print("in inner after declaring nonlocal x is ", x, " addr: ", id(x))

        x = "nonlocal"
        print("in inner after x = nonlocal x is ", x, " addr: ", id(x))
        print("inner:", x)

    inner()
    print("outer x is changed", x, 'addr is ', id(x))


outer()