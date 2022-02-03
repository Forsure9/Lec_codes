"""
Program: sum_input_Try_Execp.py

Computes the sum and average of a series of input numbers.
This program receives a series of numbers from the user and
    allows the user to press the enter key to finish providing inputs.
After the user presses the enter key, the program should print the sum of the numbers and their average

This program checks for a numeric ascii user entry. If it is a "" (enter key),
    it 'breaks' and proceed to do the sum and average, else it "continues" to get another entry
"""

sum = 0
count = 0


while True:
    number = 0
    try:
        number = input(" enter a number") # throw error here i
        sum += float(number)
        count += 1

    except ValueError:
        print(" not a number...")
        if number == "":
            print('you entered a "" to quit')
            break
        continue

print("The sum is %.2f" % (sum))


if count > 0:
    print('{0:,.2f} {1} {2} entries'.format(sum / count, 'from', count))







