
# does not handle the non digit alphabets
user_input = ''

while user_input != 'q':
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        print('Invalid weight.')
    else:
        height = int(input('Enter height (in inches): '))
        if height <= 0:
            print('Invalid height')

    if (weight < 0) or (height <= 0):
        print('Cannot compute info.')
    else:
        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")