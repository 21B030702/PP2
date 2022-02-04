def summa(s):
    cnt = 0
    for i in s:
      cnt += ord(i)
    return cnt
if summa(input()) > 300:
   print("It is tasty!")
else:
    print("Oh, no!")