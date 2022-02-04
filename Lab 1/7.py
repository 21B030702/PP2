s = input()
sum = 0
k = len(s)
for i in range(0,k):
    sum += int(s[i])*(2**(k - i))/2
print(int(sum))