def search(List, n):

    for i in range(len(List)):
        if List[i] == n:
            return True
    return False


# list which contains both string and numbers.
List = [1, 2, 'sachin', 4, 'ashu', 6]

# Driver Code
n = 'ashu'

if search(List, n):
    print("Found")
else:
    print("Not Found")
