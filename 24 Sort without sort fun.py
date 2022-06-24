my_list = ['Swanand', 'Ashutosh', 'Shreyash', 'Gaurav', 'Vishal']

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):

        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)
