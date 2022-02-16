s  = input().split()
list = []
k = 0
for i in range(len(s)):
    s[i] = int(s[i])
    list.append(s[i])
print(len(list))
for i in range(len(list)):
    i = k
    k = list[i] + i
    i = k
    print(k)
    if k >= len(list)-1:
        break
    elif list[i] == 0:
         for j in range(1,i):
             j = 1
             i = i-j
             if list[i] == 0:
                continue
             else:
                 k = i
if k >= len(list)-1:
    print('1')
else:
    print('0')
