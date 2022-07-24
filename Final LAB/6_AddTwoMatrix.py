X = [[14, 17, 13],
     [14, 15, 9],
     [7, 45, 9]]
Y = [[5, 2, 1],
     [17, 9, 13],
     [6, 10, 19]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for r in result:
    print(r)
