r = []
while True:
    s = input()
    if not s == '0':
        k = [i for i in s.split()]
        r.append(k)
    else:
        break
for i in range(len(r)):
    for j in range(len(r)):
        if int(r[i][2]) < int(r[j][2]):
            k = r[i]
            r[i] = r[j]
            r[j] = k
        elif int(r[i][2]) == int(r[j][2]):
             if int(r[i][1]) < int(r[j][1]):
                k = r[i]
                r[i] = r[j]
                r[j] = k
             elif int(r[i][1]) == int(r[j][1]):
                  if int(r[i][0]) < int(r[j][0]):
                     k = r[i]
                     r[i] = r[j]
                     r[j] = k
for x in r: 
    print(*x, sep = ' ')