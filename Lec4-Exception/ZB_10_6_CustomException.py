# Define a custom exception type
# for this program, try to trip the two exceptions (ValueError and LessThanZeroError) by
#       entering (NAN, alphabet, or -ve number)

# pass Exception (parent class) as an argument (extent from)
class LessThanZeroError(Exception):
    def __init__(self, value):
        self.value = value


try:
    my_num = int(input('Enter number: '))

    if my_num < 0:
        raise LessThanZeroError('my_num must be greater than 0')
    print("my_num is good")
except ValueError:
    print('NAN')
except LessThanZeroError:
    print("less the zero")
else:  # you can use the variable in try
    print("print after try passes")
    try:
        print("let's do another try")
        my_num = float(input('another number'))

    finally:
        print(" done trying....")
# print('my_num:', my_num)