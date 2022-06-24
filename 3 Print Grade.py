# Read Percentage from user
percentage = int(input('Enter Your Percentage : '))
if percentage >= 80:
    print('You Got O Grade')
elif percentage >= 75:
    print('You Got A+ Grade')
elif percentage >= 70:
    print('You Got A Grade')
elif percentage >= 65:
    print('You Got B+ Grade')
elif percentage >= 60:
    print('You Got B Grade')
elif percentage >= 55:
    print('You Have Passed')
else:
    print('You Have Failed')
