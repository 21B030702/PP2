
s = input()
t = input()
k = 0
max = -1e9
min =  1e9
cnt = 0
list = []
for i in range(0, len(s)):
    if  s[i] == t:
        k = i
        cnt = cnt + 1
        list.append(i)

if cnt == 1:
       print(k)

else: 
    for i in range(0,len(list)):
        if list[i] > max:
            max = list[i]
    for i in range(0,len(list)):
        if list[i] < min:
            min = list[i]
            
    print(min, max)
    

