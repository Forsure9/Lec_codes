"""
multiple ways to iterate over a list

"""

list=[1,3,5,7,8]
def for_i():
    print('for_i')
    for i in list:
        print(i, end=", ")

def for_range():
    print("\nfor_range")
    for i in range(len(list)):
        print(list[i], end=', ')

def while_i():
    print('\nwhile_i')
    i = 0
    while i < len(list):
        print(list[i], end=', ')
        i +=1

def list_compreh():
    print('\nlist comprehension - best!')
    [print(i,end = ', ') for i in list]



for_i()
for_range()
while_i()
list_compreh()


