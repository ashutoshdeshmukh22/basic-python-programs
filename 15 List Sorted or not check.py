# initializing list
test_list = [1, 4, 5, 8, 10, 12, 3]

# printing original list
print("Original list : " + str(test_list))

# using sorted() to
# check sorted list
flag = 0
if(test_list == sorted(test_list)):
    flag = 1

# printing result
if (flag):
    print("Yes, List is sorted.")
else:
    print("No, List is not sorted.")
