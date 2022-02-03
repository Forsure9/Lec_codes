
# try enter a char NOT 'q'

user_input = ''
while user_input != 'q':
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print('BMI:', bmi)
    print('(CDC: 18.6-24.9 normal)\n')
    # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")