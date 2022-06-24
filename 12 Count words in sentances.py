
count = 0
my_string = input('Enter a Sentance ')
my_char = input('Enter Character to Count ')

for i in my_string:
    if i == my_char:
        count += 1

print(count)
