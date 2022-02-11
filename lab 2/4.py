n = int(input())
a = [[0] * n for i in range(n)]
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if i == j or i > j :
                a[i][j] = "#"
            else:
                a[i][j] = "."        
else :
    for i in range(n):
        for j in range(n):
            if i+j == j+i and i+j >= n-1:
                a[i][j] = "#"
            else:
                a[i][j] = "."
for row in a:
    print(''.join([str(elem) for elem in row]))           

