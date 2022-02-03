
x= 100

def myfunc():
    y = " local y "
  #  x = x *2  # try this...
    print(" the global stuff is: ", x, "local stuff is: ", y)

myfunc()
print(" getting x from outside the function", x)