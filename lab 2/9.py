n = int(input())
x = 0
list_discs = []
list = []
for i in range(n):
    s = input().split()
    if len(s) == 2:
       x = s[0]
       y = s[1]
       list_discs.append(y)
    else:
         y = list_discs[0] 
         list_discs.remove(list_discs[0])
         list.append(y)
print(*list, sep= " ") 