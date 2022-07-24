test_string = "There are 777 , and 145 and 209"
print("The original string : " + test_string)
res = [int(i) for i in test_string.split() if i.isdigit()]
print("The numbers list is : " + str(res))
