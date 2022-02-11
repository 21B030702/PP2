n = int(input())
list_demon = []
for i in range(n):
    x, y = [i for i in input().split()]
    list_demon.append(y)
k = int(input())
for i in range(k):
    d, c, m = [j for j in input().split()]
    m = int(m)
    while m > 0 and c in list_demon:
         list_demon.remove(c)
         m -= 1
print(f'Demons left: {len(list_demon)}')
    







