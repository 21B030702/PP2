from math import *
def isprime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
l = [int(i) for i in input().split()]
dist, f = l[0], l[1]
if dist <= 500 and isprime(dist) and f % 2 == 0:
    print('Good job!')
else:
    print('Try next time!')

