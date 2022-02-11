n = int(input())
my_list = []
a = set()
for i in range(n):
    s = input()
    my_list.append(s)
t = set(my_list)
my_list.clear()
for s in t:
    if s.isalpha():
        continue
    elif s.islower():
        continue
    elif s.isdigit():
        continue
    elif any(s in ".,:;!_*-+()/#¤%&)" for s in t):
        continue
    elif s.isupper():
        continue
    else:
        a.add(s)
for s in a:
    if len(s) >= 3:
        my_list.append(s)
my_list.sort()
print(len(my_list))
for s in my_list:
    print(s)

