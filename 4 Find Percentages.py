# Python Program to Calculate Total Marks Percentage and Grade of a Student

print("Enter the marks of five subjects : ")

subject_1 = float(input('Enter Marks For First Subject - '))
subject_2 = float(input('Enter Marks For Second Subject - '))
subject_3 = float(input('Enter Marks For Third Subject - '))
subject_4 = float(input('Enter Marks For Fourth Subject - '))
subject_5 = float(input('Enter Marks For Fifth Subject - '))

percentage = 0

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500.0) * 100

# It will produce the final output
print("\nThe Total marks is: ", total, "/ 500.00")
print("The Percentage is: ", percentage, "%")
