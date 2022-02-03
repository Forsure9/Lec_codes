
'''
numeric data type represent the data which has numeric value.
Numeric value can be integer, floating number or even complex numbers.
These values are defined as int, float and complex class in Python.



Integers – This value is represented by int class.
    It contains positive or negative whole numbers (without fraction or decimal).
    In Python there is no limit to how long an integer value can be.
Float – This value is represented by float class. It is a real number with floating point representation.
    It is specified by a decimal point. Optionally,
    the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
Complex Numbers – Complex number is represented by complex class.
    It is specified as (real part) + (imaginary part)j. For example – 2+3j



'''




# Python program to demonstrate numeric value

a = 5
print("Type of a: ", type(a))
b = 5.0
print("Type of b: ", type(b))
c = 2 + 4j
sq = c*c
print("Type of c: ", type(c))
print("c*c", sq)