# from the previous ZB_10_1_2, add more exception handlers..
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('NAN,,,,Could not calculate health info.\n')
    except ZeroDivisionError:
        print(' "Divide by zero"  Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")