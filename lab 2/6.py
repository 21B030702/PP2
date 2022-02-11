n = int(input())
y = 0
list_keys = []
k = 0
max_val = 0
d1 = dict()
for i in range (n):
    s = input().split()
    x = s[0]
    y = int(s[1])
    if x not in d1:
        d1[x]=y
    else:
        d1[x]+=y
max_val = max(d1.values()) 
list_keys = list(d1.keys())
list_keys.sort()  
for i in list_keys:
    if max_val == d1[i]:
       print(i ,"is", "lucky!")
    else:
        k = max_val - d1[i] 
        print(i, "has to receive" , k , "tenge")

