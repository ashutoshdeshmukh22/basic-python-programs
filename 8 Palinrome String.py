str = input('Enter a String to check for palindrome ')
temp = ""
for i in str:
    temp = i + temp

if (str == temp):
    print(str, "is a palindrome string")
else:
    print(str, "is not a palindrome string")
