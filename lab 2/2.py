n = int(input())
s = input().split()
for i in range(0, len(s)):
    s[i] = int(s[i])
s.sort()
print(s[len(s)-1]*s[len(s)-2])

