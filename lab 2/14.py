list = []
ans = []
while True:
    numbers = int(input())
    if not numbers == 0:
        list.append(numbers)
    else:
        break
y = len(list)-1
for x in range(y+1):
    if x == y:
        ans.append(list[x])
        break
    elif x > y:
        break
    ans.append(list[x]+list[y])
    y -= 1
print(*ans)
    