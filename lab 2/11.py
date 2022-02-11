a = input()
a = a.replace("!", " ")
a = a.replace("?", " ")
a = a.replace(",", " ")
my_list = [] 
s = set(a.split())
my_list = list(s)
print(len(s))
my_list.sort()
for i in my_list:
    print(i)