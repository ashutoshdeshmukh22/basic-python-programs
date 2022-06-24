
def printHyphen(string):

    # Split by space and converting
    # String to list and
    lis = list(string.split(","))

    # joining the list and storing in string
    string = '-'.join(lis)
    # returning the string
    return string


# Driver code
string = "Ashutosh , Swaanand , Alex"
print(printHyphen(string))

# This code is contributed by vikkycirus
