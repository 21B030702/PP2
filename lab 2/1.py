s = input().split()
ok = False
k = 0
j = 0
list = []
a = []
for i in range(0, len(s)):
    s[i] = int(s[i])
    list.append(s[i])
for i in range(0, len(list)):
    i = j
    if i >= len(list):
        break
    k = list[i] + i
    j = k       
    a.append(k)
    if a[-1] >= len(s)-1:
        ok = True
print(a)
if ok == True: 
    print(1)
else :
    print(0)


