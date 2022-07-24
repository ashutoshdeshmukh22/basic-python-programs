file = input("Enter filename:")
with open(file, 'r') as f:
    words = f.read().split()
    max_length = len(max(words, key=len))
    print("Longest words in the file are")
    for word in words:
        if len(word) == max_length:
            print(word)
