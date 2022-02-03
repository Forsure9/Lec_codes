# When you declare a global keyword variable inside the nested function and
#   when you change the global keyword variable inside the nested function,
#   it will reflect outside the local scope, since it is used as a global keyword.

intX = 20
print("outside main(), intX is ", intX, id(intX))


def main():
    intX = 20
    print("main() intx address is ", id(intX)) # addr different with different content???

    def inner():
        global intX  # this takes on the intX address of outside main( )
        print("in inner() B4 change global intx is ", id(intX))
        intX = 30
        print("in inner() after change intx is ", id(intX))

    print("before calling inner() intX is:", intX, id(intX))

    inner()
    print("after  inner() intX is ", intX)
    print("after calling inner() intX is:", intX, id(intX))


main()

print(" the intX in main( ) outside the inner is ", intX, id(intX))
