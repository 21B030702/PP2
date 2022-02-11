n = int(input())
arr = [[0] * n for i in range(n)]
for i in range(0,n):
    for j in range(n):
        arr[0][j] = j
for i in range(n):
    for j in range(0,n):
        arr[i][0] = i
for i in range(n):
    for j in range(n):
        if i == j and i!= 0 and j!= 0:
            arr[i][j] = i * j
for row in arr:
    print(' '.join([str(elem) for elem in row]))
            