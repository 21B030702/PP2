a = [i for i in input()]
list = []
ok = True
for i in range(len(a)):
    if a[i] == '(' or a[i] == '[' or a[i] == '{':
        list.append(a[i])
        continue
    if a[i] == ')' and not len(list) == 0 and not list[-1] == '(':
        ok = False
        break
    elif a[i] == '}' and not len(list) == 0 and not list[-1] == '{':
        ok = False
        break
    elif a[i] == ']' and not len(list) == 0 and not list[-1] == '[':
        ok = False
        break
    elif len(list) == 0:
        ok = False
        break
    else:
        del list[-1]
if ok and len(list) == 0:
    print("Yes")
else:
    print("No")