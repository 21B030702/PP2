s = input().split()
if len(s) == 1:
    t = input().split()
list = []
a = []
n = 0
x = 0
if len(s) == 1:
    n = int(s[0])
    x = int(t[0])
else:
    for i in range(0, len(s)):
        s[i] = int(s[i])
        list.append(s[i])
    n = list[0]
    x = list[1]
for i in range(n):
    i =  x + 2*i 
    a.append(i)
for i in range(1, len(a)):
    x = x^a[i] 
print(x)