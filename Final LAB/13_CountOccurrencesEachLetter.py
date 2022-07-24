try:
    with open('hello.txt', 'r') as f:
        data = f.read().lower()
        frequency = {}
        for i in data:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        for key, value in frequency.items():
            print("Frequency of each character:", key, ':', value)

except FileNotFoundError as msg:
    print(msg)
